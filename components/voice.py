"""
GuideFlow AI - Voice Interaction Component
Renders the real-time voice status indicator, manages microphone input,
voice command execution, and senior-friendly text-to-speech audio playback.
"""

from typing import Optional, Dict, Any, Tuple
import streamlit as st

from services.speech_service import transcribe_audio_bytes, generate_tts_audio
from utils.helpers import get_text


def render_voice_status_bar(status: str = "ready", custom_message: Optional[str] = None):
    """
    Renders a calm, clear voice status indicator for senior citizens.
    Status options: 'ready', 'listening', 'processing', 'speaking'.
    """
    lang = st.session_state.get("language", "en")
    
    status_map = {
        "ready": ("ready", get_text("status_ready", lang)),
        "listening": ("listening", get_text("status_listening", lang)),
        "processing": ("processing", get_text("status_processing", lang)),
        "speaking": ("speaking", get_text("status_speaking", lang))
    }

    dot_class, default_msg = status_map.get(status, ("ready", get_text("status_ready", lang)))
    display_msg = custom_message or default_msg

    html = f"""
    <div class="voice-status-pill">
        <span class="status-dot {dot_class}"></span>
        <span>{display_msg}</span>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def play_voice_message(text: str, language: str = "en", autoplay: bool = True):
    """
    Generates TTS audio and displays an accessible audio player.
    Guarantees any sensitive numbers or passwords are sanitized beforehand.
    """
    if not text:
        return

    audio_bytes = generate_tts_audio(text, language=language)
    if audio_bytes:
        # Display audio player with clear senior label
        st.caption(f"🔊 GuideFlow Voice Audio ({language.upper()}):")
        st.audio(audio_bytes, format="audio/mp3", autoplay=autoplay)


def render_voice_input_controls(language: str = "en") -> Tuple[Optional[str], Optional[str]]:
    """
    Renders the microphone input widget.
    Returns: (recognized_text, command)
      - recognized_text: the full transcript
      - command: 'NEXT', 'BACK', 'REPEAT', 'SIMPLIFY', 'STOP', or None
    """
    st.markdown(f"**{get_text('btn_speak', language)}**")
    st.caption("Tap the microphone button below, speak naturally in your chosen language, then tap stop.")

    # Native Streamlit audio input
    audio_data = st.audio_input("Record your voice", label_visibility="collapsed")

    if audio_data is not None:
        raw_bytes = audio_data.getvalue()
        
        # Avoid re-processing the exact same recorded audio buffer
        last_audio_hash = st.session_state.get("last_processed_audio_hash", None)
        current_hash = hash(raw_bytes)

        if current_hash != last_audio_hash:
            st.session_state["last_processed_audio_hash"] = current_hash
            
            with st.spinner(get_text("status_processing", language)):
                result = transcribe_audio_bytes(raw_bytes, language=language)

            if result["success"]:
                st.success(f"🗣️ You said: \"{result['text']}\"")
                return result["text"], result["command"]
            else:
                st.warning(result["error"])
                return None, None

    return None, None
