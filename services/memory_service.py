"""
GuideFlow AI - Limited Memory & Preferences Service
Maintains transparent, privacy-conscious user preferences (Language, Theme, Font Size).
Strictly prohibits storage of passwords, OTPs, Aadhaar numbers, or financial details.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any

from utils.config import DEFAULT_LANGUAGE, DEFAULT_THEME, BASE_DIR

MEMORY_FILE = BASE_DIR / "memory_preferences.json"

DEFAULT_PREFERENCES: Dict[str, Any] = {
    "language": DEFAULT_LANGUAGE,
    "theme": DEFAULT_THEME,
    "font_size": "large",  # Senior-friendly default: large text
    "voice_speed": 0.95,
    "last_task": None
}


def load_memory() -> Dict[str, Any]:
    """Load non-sensitive preferences from local storage or fallback to defaults."""
    if not os.path.exists(MEMORY_FILE):
        return DEFAULT_PREFERENCES.copy()

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Ensure only non-sensitive whitelist keys are kept
            safe_data = {
                "language": data.get("language", DEFAULT_PREFERENCES["language"]),
                "theme": data.get("theme", DEFAULT_PREFERENCES["theme"]),
                "font_size": data.get("font_size", DEFAULT_PREFERENCES["font_size"]),
                "voice_speed": data.get("voice_speed", DEFAULT_PREFERENCES["voice_speed"]),
                "last_task": data.get("last_task", None)
            }
            return safe_data
    except Exception:
        return DEFAULT_PREFERENCES.copy()


def save_memory(preferences: Dict[str, Any]) -> bool:
    """Save updated non-sensitive preferences safely."""
    # Filter against strictly allowed keys
    safe_data = {
        "language": preferences.get("language", DEFAULT_PREFERENCES["language"]),
        "theme": preferences.get("theme", DEFAULT_PREFERENCES["theme"]),
        "font_size": preferences.get("font_size", DEFAULT_PREFERENCES["font_size"]),
        "voice_speed": preferences.get("voice_speed", DEFAULT_PREFERENCES["voice_speed"]),
        "last_task": preferences.get("last_task", None)
    }

    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(safe_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False


def clear_memory() -> bool:
    """Completely wipe remembered preferences and reset to defaults."""
    if os.path.exists(MEMORY_FILE):
        try:
            os.remove(MEMORY_FILE)
        except Exception:
            pass
    return True
