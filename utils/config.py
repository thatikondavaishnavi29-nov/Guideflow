"""
GuideFlow AI - Configuration and Environment Settings
Loads environment variables and holds application-wide defaults.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)

# Application metadata
APP_NAME = "GuideFlow AI"
APP_SUBTITLE = "A Voice-Guided Web Assistant for Senior Citizens' Online Service Navigation"
APP_TAGLINE = "See it → Speak to it → Understand it → Get guided through it"

# API Keys
def get_gemini_api_key() -> str:
    """Retrieve Gemini API key from environment or Streamlit secrets."""
    # Check OS env first
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key:
        try:
            import streamlit as st
            if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
                key = str(st.secrets["GEMINI_API_KEY"]).strip()
        except Exception:
            pass
    return key

# Supported Languages: Code -> Display Name & Native Name
SUPPORTED_LANGUAGES = {
    "en": {
        "name": "English",
        "native": "English",
        "flag": "🇬🇧",
        "stt_code": "en-IN",
        "tts_code": "en",
        "gemini_name": "English"
    },
    "te": {
        "name": "Telugu",
        "native": "తెలుగు",
        "flag": "🇮🇳",
        "stt_code": "te-IN",
        "tts_code": "te",
        "gemini_name": "Telugu"
    },
    "hi": {
        "name": "Hindi",
        "native": "हिन्दी",
        "flag": "🇮🇳",
        "stt_code": "hi-IN",
        "tts_code": "hi",
        "gemini_name": "Hindi"
    }
}

DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
if DEFAULT_LANGUAGE not in SUPPORTED_LANGUAGES:
    DEFAULT_LANGUAGE = "en"

DEFAULT_THEME = os.getenv("DEFAULT_THEME", "light").lower()
if DEFAULT_THEME not in ["light", "dark"]:
    DEFAULT_THEME = "light"

DEFAULT_SPEECH_SPEED = float(os.getenv("SPEECH_SPEED", "0.95"))

# Trusted Domain Suffixes & Pre-approved Official Portals
OFFICIAL_TRUSTED_DOMAINS = [
    # Indian Government
    "gov.in",
    "nic.in",
    "uidai.gov.in",
    "myaadhaar.uidai.gov.in",
    "epfindia.gov.in",
    "incometax.gov.in",
    "parivahan.gov.in",
    "jeevanpramaan.gov.in",
    "cowin.gov.in",
    "abdm.gov.in",
    "digitalindia.gov.in",
    "indiapost.gov.in",
    "passportindia.gov.in",
    "nvsp.in",
    "eci.gov.in",
    "voters.eci.gov.in",
    # Education & Scholarship portals
    "scholarships.gov.in",
    # Employment & Jobs
    "ncs.gov.in",
    # Food & Civil Supplies
    "nfsa.gov.in",
    # Civil Registration System
    "crsorgi.gov.in",
    # Land Records
    "dilrmp.gov.in",
    # PM-KISAN (Agriculture)
    "pmkisan.gov.in",
    # Grievance Portal
    "pgportal.gov.in",
    # State Electricity Boards (Examples)
    "tnebnet.org",
    "bescom.karnataka.gov.in",
    "bsesdelhi.com",
    "mahadiscom.in",
    "tssouthernpower.com",
    "apspdcl.in",
    # Official Healthcare & Hospitals
    "aiims.edu",
    "ors.gov.in",
    # Trusted Banking & Utilities
    "sbi.co.in",
    "onlinesbi.sbi",
    "icicibank.com",
    "hdfcbank.com",
    "irctc.co.in",
    "bharatbillpay.com"
]

# High-risk domain extensions commonly associated with scams/phishing
SUSPICIOUS_TLDS = [
    "tk", "ml", "ga", "cf", "gq", "xyz", "top", "work", "loan", "click", "fit", "buzz"
]
