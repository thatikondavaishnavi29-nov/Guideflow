"""
GuideFlow AI - Accessibility & Senior Settings Component
Controls text size, color contrast theme, speech speed, and transparent memory inspection.
"""

from typing import Dict, Any
import streamlit as st

from utils.config import SUPPORTED_LANGUAGES
from services.memory_service import load_memory, save_memory, clear_memory
from utils.helpers import get_text


def render_accessibility_sidebar() -> Dict[str, Any]:
    """
    Renders senior-friendly accessibility controls in the sidebar or top bar.
    Returns current configuration dict.
    """
    prefs = load_memory()

    with st.sidebar:
        st.markdown("### ⚙️ Senior Accessibility")
        st.caption("Customize GuideFlow to make reading and listening comfortable.")

        # 1. Language Selection (English / తెలుగు / हिन्दी)
        current_lang = st.session_state.get("language", prefs.get("language", "en"))
        lang_keys = list(SUPPORTED_LANGUAGES.keys())
        lang_labels = [f"{SUPPORTED_LANGUAGES[k]['flag']} {SUPPORTED_LANGUAGES[k]['native']} ({SUPPORTED_LANGUAGES[k]['name']})" for k in lang_keys]
        
        current_idx = lang_keys.index(current_lang) if current_lang in lang_keys else 0

        selected_label = st.selectbox(
            "🌐 Choose Language / భాష / भाषा",
            options=lang_labels,
            index=current_idx,
            help="Select your preferred language for voice and screen instructions."
        )
        selected_lang_code = lang_keys[lang_labels.index(selected_label)]

        if selected_lang_code != current_lang:
            st.session_state["language"] = selected_lang_code
            prefs["language"] = selected_lang_code
            save_memory(prefs)
            st.rerun()

        st.divider()

        # 2. Text Size Selector
        font_scale = st.radio(
            "🔍 Text Size",
            options=["regular", "large", "extra_large"],
            index=["regular", "large", "extra_large"].index(prefs.get("font_size", "large")),
            format_func=lambda x: {
                "regular": "A  Standard Size",
                "large": "A+  Large Size (Recommended)",
                "extra_large": "A++ Extra Large Size"
            }[x]
        )
        if font_scale != prefs.get("font_size"):
            prefs["font_size"] = font_scale
            save_memory(prefs)
            st.rerun()

        st.divider()

        # 3. Theme Selector (Soft & Calm Light Mode vs High-Contrast Dark Mode)
        current_theme = prefs.get("theme", "light")
        dark_mode_enabled = st.toggle("🌙 High-Contrast Dark Mode", value=(current_theme == "dark"))
        new_theme = "dark" if dark_mode_enabled else "light"

        if new_theme != current_theme:
            prefs["theme"] = new_theme
            save_memory(prefs)
            st.rerun()

        st.divider()

        # 4. Memory & Privacy Transparency
        with st.expander("🛡️ Privacy & Stored Memory", expanded=False):
            st.markdown("""
            **What GuideFlow Remembers:**
            - Your language preference
            - Your chosen text size & theme
            
            **What GuideFlow NEVER Stores:**
            - ❌ Passwords or PINs
            - ❌ Bank or OTP codes
            - ❌ Full Aadhaar numbers
            """)

            st.caption(f"Currently Saved: Language={prefs.get('language')}, Font={prefs.get('font_size')}, Theme={prefs.get('theme')}")

            if st.button("🗑️ Clear Stored Memory", use_container_width=True):
                clear_memory()
                st.session_state["language"] = "en"
                st.session_state["active_task"] = None
                st.success("Memory cleared successfully!")
                st.rerun()

    return {
        "language": selected_lang_code,
        "font_size": font_scale,
        "theme": new_theme
    }
