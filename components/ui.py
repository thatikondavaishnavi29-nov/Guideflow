"""
GuideFlow AI - Senior-Friendly UI Styling & Typography
Injects Atkinson Hyperlegible & Inter fonts, custom accessible themes (Light & Dark),
and senior-optimized styles with high contrast, large touch targets, and calming accents.
"""

import streamlit as st


def inject_custom_styles(theme: str = "light", font_scale: str = "large"):
    """
    Injects custom CSS for Google Fonts, senior-friendly themes, and responsive design.
    """
    # Font scale multiplier
    if font_scale == "extra_large":
        base_font_size = "20px"
        h1_size = "2.3rem"
        h2_size = "1.8rem"
        btn_font_size = "1.25rem"
        step_text_size = "1.4rem"
    elif font_scale == "regular":
        base_font_size = "16px"
        h1_size = "1.9rem"
        h2_size = "1.5rem"
        btn_font_size = "1.05rem"
        step_text_size = "1.15rem"
    else:  # "large" (default senior size)
        base_font_size = "18px"
        h1_size = "2.1rem"
        h2_size = "1.65rem"
        btn_font_size = "1.15rem"
        step_text_size = "1.25rem"

    # Theme colors
    if theme == "dark":
        bg_color = "#0F172A"       # Deep slate
        card_bg = "#1E293B"        # Midnight blue card
        card_border = "#334155"    # Subtle border
        text_color = "#F8FAFC"     # Clear crisp white
        text_muted = "#94A3B8"     # Soft muted gray
        primary_teal = "#38BDF8"   # Bright accessible sky blue
        primary_btn_bg = "#0284C7" # Vibrant blue
        primary_btn_text = "#FFFFFF"
        accent_bg = "#164E63"      # Dark teal container
        accent_border = "#0E7490"
        highlight_bg = "#1E3A8A"
        warning_bg = "#451A03"
        warning_border = "#B45309"
        warning_text = "#FDE68A"
        success_bg = "#064E3B"
        success_border = "#059669"
        success_text = "#A7F3D0"
    else:  # Light Mode (Default Soft & Calm)
        bg_color = "#F8FAFC"       # Very soft clean white-blue
        card_bg = "#FFFFFF"        # Pure white cards
        card_border = "#E2E8F0"    # Light slate border
        text_color = "#0F172A"     # High-contrast charcoal slate
        text_muted = "#475569"     # High readability slate
        primary_teal = "#0D9488"   # Soft calm teal
        primary_btn_bg = "#0369A1" # Trustworthy ocean blue
        primary_btn_text = "#FFFFFF"
        accent_bg = "#F0FDFA"      # Soft soothing teal tint
        accent_border = "#99F6E4"
        highlight_bg = "#EFF6FF"   # Soft blue
        warning_bg = "#FFFBEB"
        warning_border = "#F59E0B"
        warning_text = "#92400E"
        success_bg = "#F0FDF4"
        success_border = "#34D399"
        success_text = "#065F46"

    css = f"""
    <style>
    /* Import Google Fonts: Inter for general UI, Atkinson Hyperlegible for critical steps */
    @import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: {base_font_size};
        color: {text_color};
        background-color: {bg_color};
    }}

    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}

    /* Atkinson Hyperlegible applied to critical instructions, steps, and alerts */
    .hyperlegible, .step-content, .safety-card, .voice-card, .current-step-title, .simplified-box {{
        font-family: 'Atkinson Hyperlegible', sans-serif !important;
        letter-spacing: 0.02em;
        line-height: 1.6;
    }}

    /* Senior-friendly large buttons */
    .stButton > button {{
        font-family: 'Inter', sans-serif !important;
        font-size: {btn_font_size} !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.4rem !important;
        min-height: 52px !important;
        border-radius: 12px !important;
        border: 2px solid {card_border} !important;
        background-color: {card_bg} !important;
        color: {text_color} !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
        transition: all 0.15s ease-in-out !important;
        margin-bottom: 0.5rem !important;
    }}

    .stButton > button:hover {{
        border-color: {primary_teal} !important;
        color: {primary_teal} !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
    }}

    /* Primary high-contrast action button */
    .stButton > button[kind="primary"] {{
        background-color: {primary_btn_bg} !important;
        color: {primary_btn_text} !important;
        border-color: {primary_btn_bg} !important;
    }}

    /* Form controls & inputs */
    .stTextInput > div > div > input {{
        font-size: {base_font_size} !important;
        padding: 0.8rem 1rem !important;
        border-radius: 10px !important;
        border: 2px solid {card_border} !important;
        background-color: {card_bg} !important;
        color: {text_color} !important;
    }}

    /* Custom GuideFlow Header Banner */
    .guideflow-banner {{
        background: linear-gradient(135deg, {accent_bg} 0%, {highlight_bg} 100%);
        border: 2px solid {accent_border};
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    }}

    .guideflow-title {{
        font-family: 'Inter', sans-serif;
        font-size: {h1_size};
        font-weight: 700;
        color: {text_color};
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }}

    .guideflow-subtitle {{
        font-size: {base_font_size};
        color: {text_muted};
        margin-top: 0.35rem;
        margin-bottom: 0;
        line-height: 1.5;
    }}

    /* Voice Status Indicator Bar */
    .voice-status-pill {{
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.5rem 1.2rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 1rem;
        border: 1px solid {card_border};
        background-color: {card_bg};
    }}

    .status-dot {{
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }}

    .status-dot.ready {{ background-color: #10B981; }}
    .status-dot.listening {{ background-color: #3B82F6; animation: pulse 1.5s infinite; }}
    .status-dot.processing {{ background-color: #F59E0B; animation: pulse 1.2s infinite; }}
    .status-dot.speaking {{ background-color: #8B5CF6; animation: pulse 1.0s infinite; }}

    @keyframes pulse {{
        0% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(1.25); }}
        100% {{ opacity: 1; transform: scale(1); }}
    }}

    /* Current Step Hero Card */
    .step-hero-card {{
        background-color: {card_bg};
        border: 3px solid {primary_teal};
        border-radius: 16px;
        padding: 1.8rem 2rem;
        margin: 1.2rem 0;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    }}

    .step-badge {{
        background-color: {accent_bg};
        color: {primary_teal};
        font-weight: 700;
        font-size: 1.1rem;
        padding: 0.35rem 0.9rem;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 0.75rem;
        border: 1px solid {accent_border};
    }}

    .current-step-title {{
        font-size: {h2_size};
        font-weight: 700;
        color: {text_color};
        margin-bottom: 1rem;
    }}

    .step-action-text {{
        font-size: {step_text_size};
        color: {text_color};
        margin-bottom: 1.2rem;
        line-height: 1.6;
    }}

    .step-tip-box {{
        background-color: {highlight_bg};
        border-left: 5px solid {primary_teal};
        border-radius: 8px;
        padding: 1rem 1.2rem;
        font-size: {base_font_size};
        margin-top: 1rem;
    }}

    /* Simplified Explanation Box for 'I don't understand' */
    .simplified-box {{
        background-color: {accent_bg};
        border: 2px dashed {primary_teal};
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-top: 1.2rem;
    }}

    /* Safety & Privacy Badges */
    .safety-badge-verified {{
        background-color: {success_bg};
        border: 1.5px solid {success_border};
        color: {success_text};
        padding: 0.6rem 1rem;
        border-radius: 10px;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
    }}

    .safety-badge-warning {{
        background-color: {warning_bg};
        border: 2px solid {warning_border};
        color: {warning_text};
        padding: 0.8rem 1.2rem;
        border-radius: 10px;
        font-weight: 700;
        line-height: 1.5;
    }}

    .privacy-notice-bar {{
        background-color: {accent_bg};
        border: 1px solid {accent_border};
        border-radius: 8px;
        padding: 0.6rem 1rem;
        font-size: 0.95rem;
        color: {text_muted};
        margin-bottom: 1rem;
    }}

    /* Stepper List Items */
    .stepper-item {{
        padding: 0.75rem 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        border: 1px solid {card_border};
        background-color: {card_bg};
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }}

    .stepper-item.active {{
        border: 2px solid {primary_teal};
        background-color: {highlight_bg};
        font-weight: 700;
    }}

    .stepper-item.completed {{
        border-color: {card_border};
        opacity: 0.85;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
