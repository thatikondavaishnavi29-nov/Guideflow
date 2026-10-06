"""
GuideFlow AI - Visual Input Component
Manages camera capture ('Show me what you're seeing') and image/document uploads,
displays senior-friendly analysis cards, and enables voice guidance for visual tasks.
"""

from typing import Optional, Dict, Any
import streamlit as st
from PIL import Image
import io

from services.vision_service import analyze_image_input
from services.speech_service import generate_tts_audio
from components.voice import play_voice_message
from utils.helpers import get_text


def render_visual_input_section(mode: str = "camera", language: str = "en") -> Optional[Dict[str, Any]]:
    """
    Renders camera capture or file upload interface, executes vision analysis,
    and returns the structured findings.
    """
    image_bytes = None

    if mode == "camera":
        st.markdown(f"### {get_text('btn_camera', language)}")
        st.caption("Point your device camera at your computer screen, phone, or paper document and take a photo.")
        
        camera_file = st.camera_input("Take a photo", label_visibility="collapsed")
        if camera_file is not None:
            image_bytes = camera_file.getvalue()

    else:  # "upload"
        st.markdown(f"### {get_text('btn_upload', language)}")
        st.caption("Choose an image, screenshot, or photo from your computer.")
        
        uploaded_file = st.file_uploader(
            "Select an image",
            type=["png", "jpg", "jpeg", "webp"],
            label_visibility="collapsed"
        )
        if uploaded_file is not None:
            image_bytes = uploaded_file.getvalue()

    if image_bytes is not None:
        # Avoid re-running vision analysis on identical image in the same session
        img_hash = hash(image_bytes)
        cached_result = st.session_state.get(f"vision_result_{img_hash}", None)

        if cached_result is None:
            with st.spinner("Analyzing image... GuideFlow is looking at what you see."):
                analysis = analyze_image_input(image_bytes, language=language)
                st.session_state[f"vision_result_{img_hash}"] = analysis
        else:
            analysis = cached_result

        # Render preview and senior-friendly analysis
        st.divider()
        col1, col2 = st.columns([1, 1], gap="medium")

        with col1:
            st.markdown("#### 🖼️ What You Provided")
            try:
                st.image(image_bytes, use_container_width=True)
            except Exception:
                st.image(image_bytes)

        with col2:
            st.markdown("#### 💡 GuideFlow's Explanation")
            
            # Summary
            st.markdown(f"""
            <div class="step-hero-card hyperlegible" style="padding: 1.2rem; margin: 0 0 1rem 0;">
                <p style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">What I See:</p>
                <p style="font-size: 1.15rem; margin-bottom: 0;">{analysis['summary']}</p>
            </div>
            """, unsafe_allow_html=True)

            # Recommended Action
            st.markdown(f"""
            <div class="step-tip-box hyperlegible" style="margin-top: 0.5rem; margin-bottom: 1rem;">
                <strong>👉 What to do next:</strong><br>
                <span style="font-size: 1.15rem;">{analysis['action']}</span>
            </div>
            """, unsafe_allow_html=True)

            # Sensitive info advisory
            if analysis.get("sensitive_detected", False):
                st.warning("🛡️ Sensitive details detected in this image. GuideFlow has kept them protected and will not speak them aloud.")

            # Audio reading of explanation
            play_voice_message(analysis["audio_text"], language=language, autoplay=True)

        return analysis

    return None
