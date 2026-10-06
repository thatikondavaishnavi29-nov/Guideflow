"""
GuideFlow AI - Localization and Helper Utilities
Provides translations for English, Telugu, and Hindi, along with
senior-friendly voice command matching and text normalization.
"""

from typing import Dict, Any, Optional

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "app_title": {
        "en": "GuideFlow AI",
        "te": "గైడ్‌ఫ్లో AI",
        "hi": "गाइडफ्लो AI"
    },
    "app_subtitle": {
        "en": "A Voice-Guided Web Assistant for Senior Citizens",
        "te": "సీనియర్ సిటిజన్స్ కోసం వాయిస్ గైడెడ్ వెబ్ అసిస్టెంట్",
        "hi": "वरिष्ठ नागरिकों के लिए आवाज़ से चलने वाला वेब सहायक"
    },
    "greeting": {
        "en": "Hello! How can I help you today?",
        "te": "నమస్కారం! ఈరోజు నేను మీకు ఎలా సహాయం చేయగలను?",
        "hi": "नमस्ते! आज मैं आपकी क्या मदद कर सकता हूँ?"
    },
    "intro_note": {
        "en": "I am right here with you. Speak to me, show me your screen, or choose an option below.",
        "te": "నేను మీతోనే ఉన్నాను. నాతో మాట్లాడండి, మీ స్క్రీన్‌ను చూపించండి లేదా క్రింది ఎంపికలను ఎంచుకోండి.",
        "hi": "मैं आपके साथ हूँ। मुझसे बोलकर बात करें, अपनी स्क्रीन दिखाएं, या नीचे दिए गए विकल्प चुनें।"
    },
    # Main Options
    "btn_speak": {
        "en": "🎤 Speak to GuideFlow",
        "te": "🎤 గైడ్‌ఫ్లోతో మాట్లాడండి",
        "hi": "🎤 गाइडफ्लो से बोलें"
    },
    "btn_camera": {
        "en": "📷 Show me what you're seeing",
        "te": "📷 మీ స్క్రీన్‌ను నాకు చూపించండి",
        "hi": "📷 मुझे दिखाएं आप क्या देख रहे हैं"
    },
    "btn_upload": {
        "en": "📄 Upload a document/image",
        "te": "📄 పత్రం లేదా ఫోటో అప్‌లోడ్ చేయండి",
        "hi": "📄 दस्तावेज़ या फोटो अपलोड करें"
    },
    "btn_type": {
        "en": "⌨️ Type your question",
        "te": "⌨️ మీ ప్రశ్నను టైప్ చేయండి",
        "hi": "⌨️ अपना सवाल टाइप करें"
    },
    "lang_select": {
        "en": "Language / భాష / भाषा",
        "te": "భాష / Language / भाषा",
        "hi": "भाषा / Language / భాష"
    },
    # Quick tasks
    "quick_task_title": {
        "en": "Common Services for You",
        "te": "తరచుగా అవసరమయ్యే సేవలు",
        "hi": "अक्सर उपयोग की जाने वाली सेवाएं"
    },
    "task_electricity": {
        "en": "⚡ Pay Electricity Bill",
        "te": "⚡ కరెంట్ బిల్లు చెల్లింపు",
        "hi": "⚡ बिजली का बिल भरें"
    },
    "task_hospital": {
        "en": "🏥 Book Doctor Appointment",
        "te": "🏥 డాక్టర్ అపాయింట్‌మెంట్ బుక్ చేయండి",
        "hi": "🏥 डॉक्टर की अपॉइंटमेंट लें"
    },
    "task_pension": {
        "en": "🧓 Check Pension / Jeevan Pramaan",
        "te": "🧓 పెన్షన్ సర్టిఫికేట్ / జీవన్ ప్రమాణ్",
        "hi": "🧓 पेंशन स्थिति / जीवन प्रमाण पत्र"
    },
    "task_aadhaar": {
        "en": "🪪 Aadhaar Card Services",
        "te": "🪪 ఆధార్ కార్డు సేవలు",
        "hi": "🪪 आधार कार्ड सेवाएं"
    },
    "task_mobile": {
        "en": "📱 Mobile Recharge",
        "te": "📱 మొబైల్ రీఛార్జ్",
        "hi": "📱 मोबाइल रिचार्ज"
    },
    # Stepper & Navigation
    "btn_next": {
        "en": "Next Step →",
        "te": "తరువాతి దశ →",
        "hi": "अगला कदम →"
    },
    "btn_back": {
        "en": "← Previous Step",
        "te": "← మునుపటి దశ",
        "hi": "← पिछला कदम"
    },
    "btn_listen": {
        "en": "🔊 Listen Aloud",
        "te": "🔊 వినండి",
        "hi": "🔊 आवाज़ में सुनें"
    },
    "btn_repeat": {
        "en": "🔁 Repeat Step",
        "te": "🔁 మళ్లీ చెప్పండి",
        "hi": "🔁 दोहराएं"
    },
    "btn_simplify": {
        "en": "💡 I Don't Understand",
        "te": "💡 నాకు అర్థం కాలేదు (సులభంగా చెప్పండి)",
        "hi": "💡 मुझे समझ नहीं आया (सरल शब्दों में बताएं)"
    },
    "btn_stop": {
        "en": "⏹ Finish / Stop",
        "te": "⏹ ఆపండి / పూర్తి చేయండి",
        "hi": "⏹ रोकें / पूरा करें"
    },
    # Voice Status
    "status_ready": {
        "en": "GuideFlow is ready to help you.",
        "te": "గైడ్‌ఫ్లో మీకు సహాయం చేయడానికి సిద్ధంగా ఉంది.",
        "hi": "गाइडफ्लो आपकी सहायता के लिए तैयार है।"
    },
    "status_listening": {
        "en": "Listening to you... Please speak clearly.",
        "te": "వింటున్నాను... దయచేసి స్పష్టంగా మాట్లాడండి.",
        "hi": "सुन रहा हूँ... कृपया स्पष्ट आवाज़ में बोलें।"
    },
    "status_processing": {
        "en": "Thinking and preparing simple instructions...",
        "te": "ఆలోచిస్తున్నాను... సులభమైన వివరాలు సిద్ధం చేస్తున్నాను...",
        "hi": "सोच रहा हूँ... सरल निर्देश तैयार कर रहा हूँ..."
    },
    "status_speaking": {
        "en": "GuideFlow is reading instructions aloud...",
        "te": "గైడ్‌ఫ్లో వివరాలను చదివి వినిపిస్తోంది...",
        "hi": "गाइडफ्लो निर्देश पढ़कर सुना रहा है..."
    },
    # Safety & Privacy
    "privacy_banner": {
        "en": "🛡️ Privacy Protected: Sensitive numbers (Aadhaar, Bank OTPs, Passwords) are never stored or spoken aloud.",
        "te": "🛡️ గోప్యత రక్షించబడింది: ఆధార్, బ్యాంక్ OTP లేదా పాస్‌వర్డ్‌లు ఎప్పుడూ నిల్వ చేయబడవు మరియు బిగ్గరగా చదవబడవు.",
        "hi": "🛡️ गोपनीयता सुरक्षित: आधार, बैंक ओटीपी या पासवर्ड कभी भी सहेजे या जोर से बोले नहीं जाते हैं।"
    },
    "safety_warning_title": {
        "en": "⚠️ Website Safety Notice",
        "te": "⚠️ వెబ్‌సైట్ భద్రతా హెచ్చరిక",
        "hi": "⚠️ वेबसाइट सुरक्षा चेतावनी"
    },
    "safety_warning_msg": {
        "en": "Be careful. I could not verify that this is the official website. Please do not enter your bank or personal details until confirmed.",
        "te": "జాగ్రత్తగా ఉండండి. ఇది అధికారిక వెబ్‌సైట్ అని నేను నిర్ధారించలేకపోయాను. ధృవీకరించే వరకు మీ బ్యాంక్ వివరాలను నమోదు చేయవద్దు.",
        "hi": "सावधान रहें। मैं पुष्टि नहीं कर सका कि यह आधिकारिक वेबसाइट है। कृपया पुष्टि होने तक अपनी बैंक जानकारी दर्ज न करें।"
    },
    "website_verified": {
        "en": "✅ Official & Verified Website",
        "te": "✅ అధికారిక మరియు సురక్షితమైన వెబ్‌సైట్",
        "hi": "✅ आधिकारिक और सुरक्षित वेबसाइट"
    },
    "open_website": {
        "en": "🌐 Open Website in Safe View",
        "te": "🌐 వెబ్‌సైట్‌ను సురక్షితంగా తెరవండి",
        "hi": "🌐 वेबसाइट सुरक्षित रूप से खोलें"
    },
    # Errors & Fallbacks
    "err_mic": {
        "en": "I couldn't hear you clearly. Please try speaking again or type your question below.",
        "te": "నాకు స్పష్టంగా వినపడలేదు. దయచేసి మళ్లీ మాట్లాడండి లేదా క్రింద టైప్ చేయండి.",
        "hi": "मुझे स्पष्ट सुनाई नहीं दिया। कृपया पुनः बोलें या नीचे लिखकर पूछें।"
    },
    "err_general": {
        "en": "Something took longer than expected. Let's try another easy way.",
        "te": "కొంత సమయం పట్టింది. మరొక సులభమైన మార్గంలో ప్రయత్నిద్దాం.",
        "hi": "कुछ समय अधिक लग गया। आइए एक आसान तरीके से पुनः प्रयास करते हैं।"
    }
}


def get_text(key: str, lang: str = "en") -> str:
    """Retrieve localized string by key and language code."""
    if key not in TRANSLATIONS:
        return key
    lang_dict = TRANSLATIONS[key]
    return lang_dict.get(lang, lang_dict.get("en", key))


# Voice Command Definitions across all three languages
COMMAND_PATTERNS = {
    "NEXT": [
        "next", "next step", "continue", "forward", "go ahead", "proceed",
        "tarvata", "tharuvaatha", "తరువాత", "తరవాత", "ముందుకు", "తరవాతి దశ",
        "aage", "agla", "aage badho", "आगे", "अगला", "आगे बढ़ो", "अगला कदम"
    ],
    "BACK": [
        "back", "previous", "go back", "last step",
        "venuka", "munupati", "వెనుక", "మునుపటి", "వెనక్కి", "మునుపటి దశ",
        "piche", "pichla", "peechhe", "पीछे", "पिछला", "पीछे जाओ", "पिछला कदम"
    ],
    "REPEAT": [
        "repeat", "again", "say again", "once more", "listen again", "repeat step",
        "malli", "malli cheppandi", "vinandi", "మళ్లీ", "మళ్ళీ", "మళ్లీ చెప్పండి", "మరోసారి",
        "dohraen", "fir se", "dobara", "दोहराएं", "फिर से", "दोबारा", "फिर से बोलें", "दोबारा सुनें"
    ],
    "SIMPLIFY": [
        "i don't understand", "i dont understand", "dont understand", "not understanding",
        "simplify", "easier", "explain simply", "what does this mean", "i do not understand",
        "artham kaledu", "sulabhanga", "నాకు అర్థం కాలేదు", "అర్థం కాలేదు", "సులభంగా చెప్పండి", "వివరించండి",
        "samajh nahi aaya", "samajh me nahi aaya", "aasan", "samjhao", "समझ नहीं आया", "सरल करें", "आसान भाषा में बताएं"
    ],
    "STOP": [
        "stop", "halt", "pause", "cancel", "exit", "quit", "finish", "done",
        "aapu", "aapandi", "raddu", "chaloo vaddu", "ఆపు", "ఆపండి", "చాలు", "రద్దు",
        "ruko", "rok do", "khatam", "band", "रुको", "रोकें", "बंद करो", "समाप्त"
    ]
}


def parse_voice_command(text: str) -> Optional[str]:
    """
    Identifies if a spoken input matches a high-priority navigation voice command.
    Returns: 'NEXT', 'BACK', 'REPEAT', 'SIMPLIFY', 'STOP', or None if it's general query.
    """
    if not text:
        return None

    norm = text.lower().strip()
    
    # Check exact and fuzzy containment
    for action, phrases in COMMAND_PATTERNS.items():
        for phrase in phrases:
            # Match either exact, starting with, or clear command clause
            if norm == phrase or norm.startswith(phrase + " ") or norm.endswith(" " + phrase):
                return action
            if len(phrase) > 4 and phrase in norm:
                return action
                
    return None
