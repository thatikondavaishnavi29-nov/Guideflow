# GuideFlow AI 🛡️

### A Voice-Guided Web Assistant for Senior Citizens' Online Service Navigation

> **Core Philosophy:** *See it → Speak to it → Understand it → Get guided through it.*  
> GuideFlow AI is designed as a patient, reassuring digital guide sitting right beside senior citizens and non-technical adults to help them navigate complex digital services without feeling confused, overwhelmed, or hurried.

---

## 🌟 Key Features

1. **Accessibility-First Senior Interface:**
   - Designed with Google Fonts **Inter** (for UI) and **Atkinson Hyperlegible** (for all steps, warnings, and critical instructions).
   - Generous touch targets, large buttons (52px+ height), high contrast, and gentle calming colors.
   - Dual theme support: **Soft & Calm Light Mode** (default) and **High-Contrast Dark Mode**.
   - One-click Text Size scaling (Standard, Large, Extra Large).

2. **Multilingual Voice Assistant (English, Telugu, Hindi):**
   - Natural speech interaction in **English**, **Telugu (తెలుగు)**, and **Hindi (हिन्दी)**.
   - Voice navigation commands supported across all 3 languages:
     - **Next**: *"Next"*, *"తరువాత"*, *"आगे"*
     - **Back**: *"Back"*, *"వెనుక"*, *"पीछे"*
     - **Repeat**: *"Repeat"*, *"మళ్లీ చెప్పండి"*, *"दोहराएं"*
     - **I don't understand**: *"I don't understand"*, *"నాకు అర్థం కాలేదు"*, *"समझ नहीं आया"*
     - **Stop**: *"Stop"*, *"ఆపు"*, *"रुको"*
   - Crystal-clear audio pronunciation via `gTTS` with offline `pyttsx3` fallback.

3. **Structured Task Mode (Not a Generic Chatbot!):**
   - No confusing endless chat scrolling bubbles.
   - Shows all steps in a visual progress bar for total situational awareness.
   - Highlights the current step with a hero card, plain language action, and reassuring tips.
   - Audio auto-play for each step with instant replay controls.

4. **"I Don't Understand" Intelligent Simplification:**
   - When the user asks for simpler instructions, GuideFlow **never** merely repeats the same sentence.
   - It breaks down the instruction into everyday physical analogies and visual landmarks (e.g., *"Look at the top-right corner of your paper bill for the numbers in dark ink"*).
   - Reads the simpler explanation aloud.

5. **Camera & Visual Understanding:**
   - **Show me what you're seeing (📷 Camera)**: Allows seniors to take a photo of a screen, bill, or paper form.
   - **Document / Screenshot Upload (📄)**: Inspects uploaded receipts, utility bills, or website captures.
   - Explains what is visible in plain words, highlights what to click, and outlines the next action.

6. **Website Safety & Trust Verification:**
   - Automatic security checking on discovered service URLs via `tldextract`.
   - Distinguishes verified official portals (`.gov.in`, `.nic.in`, trusted electricity boards, banks) from third-party services.
   - Flags suspicious extensions (`.xyz`, `.work`, `.click`), raw IP addresses, and insecure HTTP.
   - Voice-reads loud safety warnings when an unverified link is encountered:
     > *"Be careful. I could not verify that this is the official website. Please do not enter your bank details until the website is confirmed."*

7. **Privacy & Sensitive Data Protection:**
   - Detects and masks Aadhaar numbers (`XXXX-XXXX-1234`), Credit/Debit cards (`XXXX-XXXX-XXXX-4444`), OTPs (`[OTP REDACTED]`), phone numbers, CVV, and passwords.
   - **Strict Audio Sanitization:** Sensitive numbers and passwords are **never spoken aloud** through the speakers.
   - **Transparent Limited Memory:** Stores only non-sensitive preferences (language, theme, font size). Includes a 1-click **"Clear Memory"** button.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Language** | Python 3.11.9 (compatible with Python 3.10+) |
| **Web UI** | Streamlit (`streamlit>=1.40,<2`) |
| **AI & Vision** | Google Gemini (`google-genai>=1.0,<2`), PIL (Pillow) |
| **Speech-to-Text** | `SpeechRecognition>=3.10,<4` (Google STT API engine) |
| **Text-to-Speech** | `gTTS>=2.5,<3` (multilingual audio), `pyttsx3>=2.90,<3` (offline fallback) |
| **Security & URLs** | `tldextract>=5,<6`, `requests>=2.32,<3`, `beautifulsoup4>=4.12,<5` |
| **Audio Processing**| `soundfile>=0.12,<1`, `numpy>=1.26,<3` |
| **Environment** | `python-dotenv>=1.0,<2` |

---

## 📂 Project Structure

```text
GuideFlow/
│
├── app.py                      # Main Streamlit application entry point
├── requirements.txt            # Python dependencies with required constraints
├── test_flows.py               # Comprehensive test suite covering all 8 core flows
├── .env.example                # Example environment configuration template
├── .env                        # Local configuration file (API keys & defaults)
├── .gitignore                  # Git ignore rules for Python, cache, and secrets
├── README.md                   # Beginner-friendly documentation and guide
│
├── components/                 # Streamlit UI & interaction components
│   ├── __init__.py
│   ├── ui.py                   # Custom CSS, Atkinson Hyperlegible & Inter fonts, Light/Dark theme
│   ├── voice.py                # Live Voice status bar, microphone input, audio playback
│   ├── visual_input.py         # Camera photo capture and document upload view
│   ├── guidance.py             # Step-by-step task guidance, stepper trail, simplified explanation
│   └── accessibility.py        # Senior accessibility sidebar (text scale, theme, memory)
│
├── services/                   # Application business logic & AI services
│   ├── __init__.py
│   ├── ai_service.py           # Task reasoning, clarification checks, and step simplifier
│   ├── speech_service.py       # Multilingual STT (SpeechRecognition) & TTS (gTTS + pyttsx3)
│   ├── vision_service.py       # Camera & screenshot understanding (Gemini Vision + heuristic fallback)
│   ├── web_service.py          # Online service catalog & discovery (Electricity, Doctors, Aadhaar, Pensions)
│   ├── safety_service.py       # Domain trust verification, phishing/suspicious detection
│   └── memory_service.py       # Privacy-conscious limited memory & preference persistence
│
├── utils/                      # Helper utilities
│   ├── __init__.py
│   ├── config.py               # Settings, constants, trusted domain whitelist
│   ├── privacy.py              # Sensitive data detection, redaction, audio sanitization
│   └── helpers.py              # Multilingual dictionary & multilingual voice command parser
│
└── assets/                     # Icons, mock assets, and templates
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python**: Python 3.11.9 (or Python 3.10 / 3.11).
- **Microphone**: Working microphone connected to your computer.
- **Speakers / Headphones**: Working audio output to hear voice guidance.
- **Web Browser**: Chrome, Edge, Safari, or Firefox.

### 2. Installation
Open a terminal in the project directory:

```bash
# Clone or navigate to the directory
cd Guideflow

# Install required dependencies
pip install -r requirements.txt
```

### 3. Configure API Key (Optional but Recommended)
GuideFlow works out-of-the-box with built-in verified service guides and speech synthesis. For full AI reasoning and visual screen understanding, configure your free Google Gemini API key:

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and paste your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   *(Get your API key for free from [Google AI Studio](https://aistudio.google.com/)).*

### 4. Running the Application
Launch the Streamlit app:

```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

---

## 🎙️ Enabling Microphone & Camera Access in Your Browser

1. When you click **"🎤 Speak to GuideFlow"** or **"📷 Show me what you're seeing"**, your browser will show a prompt asking for permission:
   - Click **"Allow"** on the popup.
2. If blocked, look at the **lock icon (🔒)** in your browser address bar (top left), click it, and ensure **Microphone** and **Camera** are set to **Allow**.
3. Speak clearly into the microphone. Tap the button when finished speaking.

---

## 🧪 Automated Verification Test Suite

GuideFlow includes an automated verification script testing all 8 mandatory product flows:

```bash
python test_flows.py
```

### Verified Test Cases:
1. **Text Query**: *"How can I pay my electricity bill?"* -> Verified Bharat BillPay portal + 5 structured steps.
2. **Voice Simulation**: *"I want to book a hospital appointment"* -> AIIMS/ORS portal + spoken audio response.
3. **Screenshot Understanding**: Webpage UI elements, input field pointers, and action recommendations.
4. **"I don't understand" Simplification**: Re-explains using plain words and analogies without repeating original sentences.
5. **Multilingual Test**: Full translation & TTS audio synthesis in English, Telugu, and Hindi.
6. **Sensitive Information Guard**: Redacts Aadhaar, credit card, phone, OTP, and passwords; sanitizes TTS so numbers are never spoken.
7. **Unsafe Website Detection**: Blocks suspicious `.xyz` and raw IP links with high-priority spoken safety warnings.
8. **Voice Commands**: Evaluates *"Next"*, *"Back"*, *"Repeat"*, *"I don't understand"*, and *"Stop"* in all 3 languages.

---

## 🛡️ Privacy & Security Commitments

- **No Credential Storage:** GuideFlow never asks for, records, or stores your passwords, OTP codes, CVVs, or full Aadhaar numbers.
- **Audio Sanitization:** Sensitive numbers are never spoken aloud over the device speakers.
- **Side-by-Side Guidance:** GuideFlow opens official portals in safe windows alongside your guidance card. It does **not** take control of your mouse or secretly submit financial transactions on your behalf.
- **Transparent Memory:** Users can inspect what is stored and click **"Clear Stored Memory"** at any time.

---

## ⚠️ Known Limitations & Helpful Tips

- **Browser Permissions:** Browsers require explicit user consent to access the microphone and camera. If recording fails, check browser permission settings.
- **Ambient Noise:** For optimal speech recognition accuracy, speak at a normal conversational volume in a reasonably quiet environment.
- **Offline Mode:** If an internet connection is unavailable, speech recognition falls back to text input, and audio falls back to local text-to-speech.

---

## 🔮 Future Improvements

- Browser extension sidecar for direct page highlight overlays on live websites.
- Support for additional regional Indian languages (Tamil, Kannada, Marathi, Bengali).
- Physical tactile controller integration (USB big-button accessibility remotes).
