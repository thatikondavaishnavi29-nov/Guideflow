"""
GuideFlow AI - A Voice-Guided Web Assistant for Senior Citizens' Online Service Navigation
Main Streamlit Application
"""

import streamlit as st

# Configure Streamlit page settings early
st.set_page_config(
    page_title="GuideFlow AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Core module imports
from utils.config import (
    APP_NAME, APP_SUBTITLE, APP_TAGLINE,
    SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE
)
from utils.helpers import get_text, parse_voice_command
from services.memory_service import load_memory, save_memory
from services.ai_service import generate_task_guidance, check_for_unclear_request
from services.speech_service import transcribe_audio_bytes, generate_tts_audio
from components.ui import inject_custom_styles
from components.voice import (
    render_voice_status_bar, play_voice_message, render_voice_input_controls
)
from components.visual_input import render_visual_input_section
from components.guidance import render_task_guidance_view
from components.accessibility import render_accessibility_sidebar


def init_session_state():
    """Initialize Streamlit session state variables with persistent preferences."""
    prefs = load_memory()
    
    if "language" not in st.session_state:
        st.session_state["language"] = prefs.get("language", DEFAULT_LANGUAGE)
    if "theme" not in st.session_state:
        st.session_state["theme"] = prefs.get("theme", "light")
    if "font_size" not in st.session_state:
        st.session_state["font_size"] = prefs.get("font_size", "large")
    if "active_mode" not in st.session_state:
        st.session_state["active_mode"] = "home"  # 'home', 'speak', 'camera', 'upload', 'type'
    if "active_task" not in st.session_state:
        st.session_state["active_task"] = None
    if "current_step_idx" not in st.session_state:
        st.session_state["current_step_idx"] = 0
    if "clarification_data" not in st.session_state:
        st.session_state["clarification_data"] = None
    if "voice_status" not in st.session_state:
        st.session_state["voice_status"] = "ready"
    if "voice_intro_spoken" not in st.session_state:
        st.session_state["voice_intro_spoken"] = False


def main():
    init_session_state()

    # Render Accessibility Controls in Sidebar & update settings
    acc_settings = render_accessibility_sidebar()
    lang = st.session_state["language"]
    theme = acc_settings["theme"]
    font_scale = acc_settings["font_size"]

    # Inject senior-friendly CSS, typography & colors
    inject_custom_styles(theme=theme, font_scale=font_scale)

    # Top Header & Brand Banner
    st.markdown(f"""
    <div class="guideflow-banner">
        <div class="guideflow-title">
            <span>🛡️</span>
            <span>{APP_NAME}</span>
            <span style="font-size: 1.1rem; font-weight: normal; margin-left: auto; color: #0D9488;">
                {SUPPORTED_LANGUAGES[lang]['flag']} {SUPPORTED_LANGUAGES[lang]['native']}
            </span>
        </div>
        <p class="guideflow-subtitle">{get_text('app_subtitle', lang)}</p>
    </div>
    """, unsafe_allow_html=True)

    # Privacy Protection Banner
    st.markdown(f"""
    <div class="privacy-notice-bar hyperlegible">
        {get_text('privacy_banner', lang)}
    </div>
    """, unsafe_allow_html=True)

    # Real-Time Voice Status Indicator
    render_voice_status_bar(status=st.session_state["voice_status"])

    # ROUTING LOGIC:
    # 1. If an active task is running, show the Task Guidance View
    if st.session_state["active_task"] is not None:
        render_task_guidance_view(st.session_state["active_task"], language=lang)
        return

    # 2. If an ambiguous request needs clarification
    if st.session_state["clarification_data"] is not None:
        render_clarification_view(st.session_state["clarification_data"], language=lang)
        return

    # 3. Otherwise, render the First Screen / Home Screen
    render_home_screen(lang=lang)


def render_home_screen(lang: str):
    """
    Renders the welcoming First Screen.
    Immediately displays:
    - Logo / Greeting: 'Hello! How can I help you today?'
    - The main interaction options clearly and directly:
      1. 🎤 Speak to GuideFlow
      2. 📷 Show me what you're seeing
      3. 📄 Upload a document/image
      4. ⌨️ Type your question
      5. Language selector (available in sidebar + quick buttons)
    - Quick-start service shortcuts for seniors.
    """
    st.markdown(f"<h2 class='hyperlegible' style='font-size: 2rem; margin-bottom: 0.2rem;'>{get_text('greeting', lang)}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='hyperlegible' style='font-size: 1.25rem; color: #475569; margin-bottom: 1.5rem;'>{get_text('intro_note', lang)}</p>", unsafe_allow_html=True)

    # Seven Main Interaction Choices (Presented clearly in large, prominent touch targets)
    st.markdown("### How would you like to interact?")
    col1, col2, col3, col4 = st.columns(4, gap="medium")

    with col1:
        if st.button(get_text("btn_speak", lang), key="btn_mode_speak", use_container_width=True, type="primary"):
            st.session_state["active_mode"] = "speak"
            st.session_state["voice_status"] = "listening"
            st.session_state["voice_intro_spoken"] = False
            st.rerun()

    with col2:
        if st.button(get_text("btn_camera", lang), key="btn_mode_camera", use_container_width=True):
            st.session_state["active_mode"] = "camera"
            st.rerun()

    with col3:
        if st.button(get_text("btn_upload", lang), key="btn_mode_upload", use_container_width=True):
            st.session_state["active_mode"] = "upload"
            st.rerun()

    with col4:
        if st.button(get_text("btn_type", lang), key="btn_mode_type", use_container_width=True):
            st.session_state["active_mode"] = "type"
            st.rerun()

    st.write("")

    # INTERACTION PANELS BASED ON USER CHOICE
    mode = st.session_state.get("active_mode", "home")

    if mode == "speak":
        st.divider()
        st.markdown(f"### 🎤 {get_text('btn_speak', lang)}")
        
        # GuideFlow conversational response
        intro_reply = {
            "en": "Sure. Tell me what you need help with.",
            "te": "తప్పకుండా. మీకు ఏ విషయంలో సహాయం కావాలో చెప్పండి.",
            "hi": "ज़रूर। बताइए आज मैं आपकी क्या मदद करूँ।"
        }.get(lang, "Sure. Tell me what you need help with.")

        st.info(f"🗣️ GuideFlow: \"{intro_reply}\"")
        if not st.session_state.get("voice_intro_spoken", False):
            play_voice_message(intro_reply, language=lang, autoplay=True)
            st.session_state["voice_intro_spoken"] = True

        spoken_text, cmd = render_voice_input_controls(language=lang)
        if spoken_text:
            st.session_state["voice_status"] = "processing"
            handle_query_submission(spoken_text, language=lang)

    elif mode == "camera":
        st.divider()
        render_visual_input_section(mode="camera", language=lang)

    elif mode == "upload":
        st.divider()
        render_visual_input_section(mode="upload", language=lang)

    elif mode == "type":
        st.divider()
        st.markdown(f"### ⌨️ {get_text('btn_type', lang)}")
        
        with st.form("type_question_form"):
            placeholder_text = {
                "en": "e.g., How can I pay my electricity bill?",
                "te": "ఉదాహరణ: కరెంట్ బిల్లు ఎలా చెల్లించాలి?",
                "hi": "उदाहरण: बिजली का बिल कैसे भरें?"
            }.get(lang, "How can I help you?")

            typed_query = st.text_input(
                "Enter your question:",
                placeholder=placeholder_text,
                label_visibility="collapsed"
            )
            submit_btn = st.form_submit_button("Ask GuideFlow →", type="primary", use_container_width=False)
            
            if submit_btn and typed_query.strip():
                handle_query_submission(typed_query.strip(), language=lang)

    st.divider()

    # Quick Common Services for Senior Citizens
    st.markdown(f"### 📌 {get_text('quick_task_title', lang)}")
    st.caption("Tap any service below for instant official step-by-step guidance:")

    qcol1, qcol2, qcol3 = st.columns(3, gap="small")

    with qcol1:
        if st.button(get_text("task_aadhaar", lang), key="qtask_aadh", use_container_width=True):
            handle_query_submission("Aadhaar card uidai myaadhaar", language=lang)

        if st.button(get_text("task_electricity", lang), key="qtask_elec", use_container_width=True):
            handle_query_submission("electricity bill payment bharat billpay", language=lang)

    with qcol2:
        if st.button("📜 Scholarship (NSP)", key="qtask_scholar", use_container_width=True):
            handle_query_submission("scholarship national scholarship portal", language=lang)

        if st.button(get_text("task_pension", lang), key="qtask_pens", use_container_width=True):
            handle_query_submission("pension jeevan pramaan life certificate", language=lang)

    with qcol3:
        if st.button("🛂 Passport Seva", key="qtask_pass", use_container_width=True):
            handle_query_submission("passport apply passportindia", language=lang)

        if st.button(get_text("task_hospital", lang), key="qtask_hosp", use_container_width=True):
            handle_query_submission("hospital appointment ORS doctor", language=lang)



def render_clarification_view(clarification: dict, language: str):
    """
    Renders large button choices when an inquiry is ambiguous,
    preventing AI guesswork and keeping the senior user in control.
    """
    st.markdown("### 🤔 Let's make sure I guide you to the right place")
    st.markdown(f"<div class='step-hero-card hyperlegible' style='font-size: 1.35rem;'>{clarification['question']}</div>", unsafe_allow_html=True)
    
    play_voice_message(clarification["audio_text"], language=language, autoplay=True)

    st.write("")
    st.markdown("**Please tap one of these options:**")

    cols = st.columns(len(clarification["options"]))
    for i, opt in enumerate(clarification["options"]):
        with cols[i]:
            if st.button(opt["label"], key=f"clarify_opt_{i}", use_container_width=True, type="primary" if i == 0 else "secondary"):
                st.session_state["clarification_data"] = None
                handle_query_submission(opt["query"], language=language)

    st.write("")
    if st.button("← Cancel and go back to home", key="btn_cancel_clarify"):
        st.session_state["clarification_data"] = None
        st.session_state["active_mode"] = "home"
        st.rerun()


def handle_query_submission(query_text: str, language: str):
    """
    Routes user query to AI reasoning and service discovery.
    Transitions seamlessly into Task Guidance mode or Clarification mode.
    """
    with st.spinner("Finding the best safe instructions for you..."):
        result = generate_task_guidance(query_text, language=language)

    if result["type"] == "CLARIFICATION":
        st.session_state["clarification_data"] = result["data"]
        st.session_state["active_task"] = None
        st.session_state["voice_status"] = "ready"
        st.rerun()

    elif result["type"] == "TASK":
        st.session_state["active_task"] = result
        st.session_state["current_step_idx"] = 0
        st.session_state["clarification_data"] = None
        st.session_state["voice_status"] = "speaking"
        
        # Save last task to memory
        prefs = load_memory()
        prefs["last_task"] = result["title"]
        save_memory(prefs)
        
        st.rerun()


if __name__ == "__main__":
    main()
