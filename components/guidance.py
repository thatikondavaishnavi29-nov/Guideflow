"""
GuideFlow AI - Step-by-Step Task Guidance Component
Renders the complete task guidance view for senior citizens, highlighting the current step,
displaying full situational progress, managing audio playback, and handling 'I don't understand'.
"""

from typing import Dict, Any, Optional
import streamlit as st

from services.ai_service import simplify_step_explanation
from services.speech_service import generate_tts_audio
from components.voice import play_voice_message, render_voice_input_controls
from utils.helpers import get_text, parse_voice_command


def render_task_guidance_view(task_data: Dict[str, Any], language: str = "en"):
    """
    Renders the structured task guidance mode.
    Shows all steps, highlights the current step, provides voice/click controls,
    and simplifies instructions when the user indicates confusion.
    """
    steps = task_data.get("steps", [])
    total_steps = len(steps)
    current_idx = st.session_state.get("current_step_idx", 0)

    # Ensure index bounds
    if current_idx < 0:
        current_idx = 0
    elif current_idx >= total_steps:
        current_idx = total_steps - 1
    st.session_state["current_step_idx"] = current_idx

    current_step = steps[current_idx] if steps else {}

    # Task Header
    st.markdown(f"## 📋 {task_data.get('title', 'Task Guidance')}")
    st.markdown(f"<p class='hyperlegible' style='font-size: 1.2rem; color: #475569;'>{task_data.get('description', '')}</p>", unsafe_allow_html=True)

    # Category & Government Level badges (shown when available from catalogue)
    category = task_data.get("category", "")
    gov_level = task_data.get("government_level", "")
    department = task_data.get("department", "")
    india_gov_ref = task_data.get("india_gov_reference", "")

    badge_html = ""
    if category:
        badge_html += f"<span style='background:#E0F2FE;color:#0369A1;border-radius:6px;padding:3px 10px;font-size:0.88rem;font-weight:600;margin-right:6px;'>🏷️ {category}</span>"
    if gov_level:
        badge_color = "#D1FAE5" if gov_level == "Central" else "#FEF3C7"
        text_color  = "#065F46" if gov_level == "Central" else "#92400E"
        badge_html += f"<span style='background:{badge_color};color:{text_color};border-radius:6px;padding:3px 10px;font-size:0.88rem;font-weight:600;margin-right:6px;'>🏛️ {gov_level} Government</span>"
    if india_gov_ref:
        badge_html += f"<a href='{india_gov_ref}' target='_blank' style='background:#F3E8FF;color:#6B21A8;border-radius:6px;padding:3px 10px;font-size:0.88rem;font-weight:600;text-decoration:none;'>🇮🇳 india.gov.in</a>"
    if badge_html:
        st.markdown(f"<div style='margin-bottom:0.6rem;'>{badge_html}</div>", unsafe_allow_html=True)
    if department:
        st.markdown(f"<p style='font-size:0.85rem;color:#64748B;margin-bottom:0.8rem;'>🏢 {department}</p>", unsafe_allow_html=True)

    # Website Safety & Direct Link Banner
    safety = task_data.get("safety", {})
    target_url = task_data.get("url", "")

    col_safety, col_link = st.columns([2, 1], gap="medium")
    with col_safety:
        if safety.get("status") == "VERIFIED":
            st.markdown(f"""
            <div class="safety-badge-verified hyperlegible">
                <span>{safety.get('badge', '🛡️ Verified Official')}</span> &bull; 
                <span>{safety.get('description', 'Official portal verified for safe navigation.')}</span>
            </div>
            """, unsafe_allow_html=True)
        elif safety.get("status") == "WARNING":
            st.markdown(f"""
            <div class="safety-badge-warning hyperlegible">
                <strong>{safety.get('title', '⚠️ Safety Warning')}:</strong><br>
                <span>{safety.get('description', 'Please be cautious. Do not enter passwords or bank details.')}</span>
            </div>
            """, unsafe_allow_html=True)
            # Voice-read safety warning if flagged
            if safety.get("voice_warning"):
                play_voice_message(safety["voice_warning"], language=language, autoplay=True)

    with col_link:
        if target_url:
            st.link_button(
                f"🌐 {get_text('open_website', language)}",
                url=target_url,
                help="Opens the official service website in a new tab so GuideFlow can guide you alongside it.",
                use_container_width=True
            )

    st.write("")

    # Progress & Stepper Overview (shows ALL steps for situational awareness)
    st.markdown(f"**Step {current_idx + 1} of {total_steps}**")
    
    # Render all steps overview in a clean visual trail
    stepper_cols = st.columns(total_steps)
    for i, s in enumerate(steps):
        with stepper_cols[i]:
            if i < current_idx:
                status_icon = "✅"
                card_style = "border: 2px solid #10B981; background-color: #ECFDF5;"
            elif i == current_idx:
                status_icon = "👉"
                card_style = "border: 3px solid #0D9488; background-color: #F0FDFA; font-weight: bold;"
            else:
                status_icon = "⚪"
                card_style = "border: 1px solid #CBD5E1; opacity: 0.75;"

            st.markdown(f"""
            <div style="border-radius: 8px; padding: 0.5rem 0.6rem; text-align: center; font-size: 0.95rem; {card_style}">
                <span>{status_icon} Step {i + 1}</span><br>
                <small style="line-height: 1.2; display: block; margin-top: 3px;">{s.get('title', '')[:28]}...</small>
            </div>
            """, unsafe_allow_html=True)

    # CURRENT STEP HERO CARD (Atkinson Hyperlegible for supreme senior readability)
    step_title = current_step.get("title", f"Step {current_idx + 1}")
    step_action = current_step.get("action", "")
    step_tip = current_step.get("tip", "")

    st.markdown(f"""
    <div class="step-hero-card hyperlegible">
        <div class="step-badge">CURRENT STEP &bull; {current_idx + 1} of {total_steps}</div>
        <div class="current-step-title">{step_title}</div>
        <div class="step-action-text">{step_action}</div>
        <div class="step-tip-box">
            <strong>💡 Helpful Tip:</strong> {step_tip}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Simplified Explanation Box (If 'I don't understand' is active for this step)
    is_simplified = st.session_state.get(f"simplified_step_{current_idx}", False)
    if is_simplified:
        simplified_info = st.session_state.get(f"simplified_data_{current_idx}", None)
        if not simplified_info:
            simplified_info = simplify_step_explanation(current_step, language=language)
            st.session_state[f"simplified_data_{current_idx}"] = simplified_info

        st.markdown(f"""
        <div class="simplified-box hyperlegible">
            <h4 style="color: #0D9488; margin-top: 0;">💡 Simpler, Easier Explanation:</h4>
            <p style="font-size: 1.3rem; line-height: 1.6; margin-bottom: 0;">
                {simplified_info['simpler_text']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Voice read the simpler explanation
        play_voice_message(simplified_info["audio_text"], language=language, autoplay=True)
    else:
        # Voice read standard step instructions on first render
        spoken_step_text = f"Step {current_idx + 1}: {step_title}. {step_action}. Tip: {step_tip}"
        play_voice_message(spoken_step_text, language=language, autoplay=False)

    st.write("")

    # STEP CONTROLS (Large, clear buttons with icons and text labels)
    ctrl_col1, ctrl_col2, ctrl_col3, ctrl_col4, ctrl_col5 = st.columns([1.2, 1.4, 1.2, 1.2, 1.2], gap="small")

    with ctrl_col1:
        # Listen / Repeat button
        if st.button(get_text("btn_listen", language), key="btn_listen_current", use_container_width=True):
            speech_to_play = (
                st.session_state.get(f"simplified_data_{current_idx}", {}).get("audio_text")
                if is_simplified else
                f"Step {current_idx + 1}: {step_title}. {step_action}. Tip: {step_tip}"
            )
            play_voice_message(speech_to_play, language=language, autoplay=True)

    with ctrl_col2:
        # "I don't understand" button
        if st.button(get_text("btn_simplify", language), key="btn_dont_understand", use_container_width=True):
            st.session_state[f"simplified_step_{current_idx}"] = True
            st.session_state[f"simplified_data_{current_idx}"] = simplify_step_explanation(current_step, language=language)
            st.rerun()

    with ctrl_col3:
        # Back button
        if st.button(get_text("btn_back", language), key="btn_prev_step", disabled=(current_idx <= 0), use_container_width=True):
            st.session_state["current_step_idx"] = max(0, current_idx - 1)
            st.rerun()

    with ctrl_col4:
        # Next button
        if current_idx < total_steps - 1:
            if st.button(get_text("btn_next", language), key="btn_next_step", type="primary", use_container_width=True):
                st.session_state["current_step_idx"] = current_idx + 1
                st.rerun()
        else:
            # Final Step Finish
            if st.button("🎉 Task Completed", key="btn_complete_step", type="primary", use_container_width=True):
                st.balloons()
                st.success("Congratulations! You have completed all the steps for this task.")

    with ctrl_col5:
        # Stop / Exit button
        if st.button(get_text("btn_stop", language), key="btn_stop_guidance", use_container_width=True):
            st.session_state["active_task"] = None
            st.session_state["current_step_idx"] = 0
            st.rerun()

    # Voice Command Listener on Step Screen
    st.write("")
    with st.expander("🎤 Speak Voice Command ('Next', 'Back', 'Repeat', 'I don't understand', 'Stop')", expanded=False):
        voice_text, voice_cmd = render_voice_input_controls(language=language)
        if voice_cmd or voice_text:
            cmd = voice_cmd or parse_voice_command(voice_text)
            if cmd == "NEXT" and current_idx < total_steps - 1:
                st.session_state["current_step_idx"] = current_idx + 1
                st.rerun()
            elif cmd == "BACK" and current_idx > 0:
                st.session_state["current_step_idx"] = current_idx - 1
                st.rerun()
            elif cmd == "REPEAT":
                speech_to_play = f"Step {current_idx + 1}: {step_title}. {step_action}. Tip: {step_tip}"
                play_voice_message(speech_to_play, language=language, autoplay=True)
            elif cmd == "SIMPLIFY":
                st.session_state[f"simplified_step_{current_idx}"] = True
                st.session_state[f"simplified_data_{current_idx}"] = simplify_step_explanation(current_step, language=language)
                st.rerun()
            elif cmd == "STOP":
                st.session_state["active_task"] = None
                st.session_state["current_step_idx"] = 0
                st.rerun()
