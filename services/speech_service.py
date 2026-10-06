"""
GuideFlow AI - Speech Recognition and Text-To-Speech Service
Supports Speech-to-Text (STT) and Text-to-Speech (TTS) for English, Telugu, and Hindi.
Ensures sensitive details are sanitized before any speech audio is synthesized.
"""

import io
import os
import tempfile
import hashlib
from typing import Optional, Dict, Any

import speech_recognition as sr
from gtts import gTTS

from utils.config import SUPPORTED_LANGUAGES, DEFAULT_SPEECH_SPEED
from utils.privacy import sanitize_for_tts
from utils.helpers import get_text, parse_voice_command

# In-memory cache for generated TTS audio to provide instant playback
_TTS_CACHE: Dict[str, bytes] = {}

# Initialize Speech Recognizer
_recognizer = sr.Recognizer()
_recognizer.pause_threshold = 1.0
_recognizer.phrase_threshold = 0.3
_recognizer.energy_threshold = 300


def get_stt_language_code(lang_code: str) -> str:
    """Return the Google Speech Recognition language code."""
    config = SUPPORTED_LANGUAGES.get(lang_code, SUPPORTED_LANGUAGES["en"])
    return config["stt_code"]


def get_tts_language_code(lang_code: str) -> str:
    """Return the gTTS language code."""
    config = SUPPORTED_LANGUAGES.get(lang_code, SUPPORTED_LANGUAGES["en"])
    return config["tts_code"]


def transcribe_audio_bytes(audio_bytes: bytes, language: str = "en") -> Dict[str, Any]:
    """
    Transcribes audio bytes (e.g. from Streamlit st.audio_input) to text.
    Handles English, Telugu, and Hindi with senior-friendly error responses.
    """
    if not audio_bytes or len(audio_bytes) < 100:
        return {
            "success": False,
            "text": "",
            "command": None,
            "error": get_text("err_mic", language)
        }

    stt_lang = get_stt_language_code(language)

    # Write to a temporary file for speech_recognition processing
    suffix = ".wav"
    # Streamlit audio_input usually provides WAV format
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp_file:
        tmp_path = tmp_file.name
        tmp_file.write(audio_bytes)

    try:
        with sr.AudioFile(tmp_path) as source:
            # Adjust for ambient noise and record
            _recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio_data = _recognizer.record(source)

        # Recognize using Google Speech Recognition
        text = _recognizer.recognize_google(audio_data, language=stt_lang)
        text = text.strip()

        # Check if the recognized text is a voice command
        cmd = parse_voice_command(text)

        return {
            "success": True,
            "text": text,
            "command": cmd,
            "error": None
        }

    except sr.UnknownValueError:
        return {
            "success": False,
            "text": "",
            "command": None,
            "error": get_text("err_mic", language)
        }
    except sr.RequestError as e:
        # Network or service unreachable
        return {
            "success": False,
            "text": "",
            "command": None,
            "error": get_text("err_general", language)
        }
    except Exception as e:
        return {
            "success": False,
            "text": "",
            "command": None,
            "error": get_text("err_mic", language)
        }
    finally:
        # Cleanup temporary audio file
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass


def generate_tts_audio(text: str, language: str = "en") -> Optional[bytes]:
    """
    Synthesizes speech audio from text using gTTS with caching.
    Ensures any sensitive numbers/passwords are sanitized before speech generation.
    Returns MP3 audio bytes or None if synthesis fails.
    """
    if not text or not text.strip():
        return None

    # Step 1: Sanitize text for privacy (no sensitive numbers read aloud)
    clean_text = sanitize_for_tts(text)
    if not clean_text:
        return None

    tts_lang = get_tts_language_code(language)
    cache_key = f"{tts_lang}:{hashlib.md5(clean_text.encode('utf-8')).hexdigest()}"

    if cache_key in _TTS_CACHE:
        return _TTS_CACHE[cache_key]

    # Generate audio using gTTS
    try:
        tts = gTTS(text=clean_text, lang=tts_lang, slow=False)
        audio_stream = io.BytesIO()
        tts.write_to_fp(audio_stream)
        audio_stream.seek(0)
        audio_bytes = audio_stream.read()

        # Store in cache
        _TTS_CACHE[cache_key] = audio_bytes
        return audio_bytes

    except Exception as e:
        # Fallback to pyttsx3 for English if gTTS fails (e.g., offline)
        if language == "en":
            try:
                import pyttsx3
                engine = pyttsx3.init()
                engine.setProperty('rate', int(150 * DEFAULT_SPEECH_SPEED))
                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_out:
                    tmp_out_path = tmp_out.name
                engine.save_to_file(clean_text, tmp_out_path)
                engine.runAndWait()
                
                with open(tmp_out_path, "rb") as f:
                    audio_bytes = f.read()
                try:
                    os.remove(tmp_out_path)
                except Exception:
                    pass
                    
                _TTS_CACHE[cache_key] = audio_bytes
                return audio_bytes
            except Exception:
                pass
        return None
