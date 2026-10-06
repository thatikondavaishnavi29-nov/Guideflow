"""
GuideFlow AI - AI Reasoning & Task Guidance Service
Understands senior citizen requests, clarifies ambiguous requests,
generates step-by-step guidance, and produces simplified explanations
when the senior says 'I don't understand'.
"""

import json
from typing import Dict, Any, List, Optional

from utils.config import get_gemini_api_key, SUPPORTED_LANGUAGES
from utils.privacy import redact_sensitive_text, sanitize_for_tts
from utils.helpers import get_text
from services.web_service import discover_online_service, VERIFIED_SERVICES_CATALOG
from services.safety_service import verify_website_safety


# Ambiguous query detection patterns for polite clarification
UNCLEAR_INTENTS: List[Dict[str, Any]] = [
    {
        "patterns": ["pay something", "pay bill", "want to pay", "బిల్లు చెల్లించు", "చెల్లించాలి", "बिल भरना है", "भुगतान"],
        "question": {
            "en": "What kind of bill would you like to pay today?",
            "te": "ఈరోజు మీరు ఏ రకమైన బిల్లు చెల్లించాలనుకుంటున్నారు?",
            "hi": "आज आप किस प्रकार का बिल भरना चाहते हैं?"
        },
        "options": [
            {"label": "⚡ Electricity Bill", "query": "Pay Electricity Bill"},
            {"label": "📱 Mobile Recharge", "query": "Mobile Recharge"},
            {"label": "💧 Water Bill", "query": "Pay Water Bill"},
            {"label": "🔍 Something Else", "query": "General Bill Payment"}
        ]
    },
    {
        "patterns": ["book something", "appointment", "want to book", "అపాయింట్‌మెంట్", "బుక్ చేయాలి", "बुकिंग"],
        "question": {
            "en": "What would you like to book?",
            "te": "మీరు ఏమి బుక్ చేయాలనుకుంటున్నారు?",
            "hi": "आप क्या बुक करना चाहते हैं?"
        },
        "options": [
            {"label": "🏥 Doctor Appointment (AIIMS/ORS)", "query": "Book hospital doctor appointment"},
            {"label": "🚆 Train Ticket (IRCTC)", "query": "Book train ticket"},
            {"label": "⛽ Gas Cylinder Refill", "query": "Book LPG gas cylinder"},
            {"label": "🔍 Something Else", "query": "General online booking"}
        ]
    }
]


def check_for_unclear_request(query: str, language: str = "en") -> Optional[Dict[str, Any]]:
    """
    Checks if the user's inquiry is too broad/ambiguous and returns
    clear, large button choices to prevent confusion or guesswork.
    """
    if not query:
        return None

    query_lower = query.lower().strip()
    
    # If the query is very short or matches ambiguous triggers
    for item in UNCLEAR_INTENTS:
        # If query matches an ambiguous trigger and doesn't specify details
        matched_trigger = any(p in query_lower for p in item["patterns"])
        specific_keywords = [
            "electricity", "power", "hospital", "doctor", "pension", "jeevan", "aadhaar", "water", "gas", "train", "mobile",
            "కరెంట్", "విద్యుత్", "ఆసుపత్రి", "డాక్టర్", "పెన్షన్", "ఆధార్", "నీటి", "గ్యాస్", "రైలు", "మొబైల్",
            "बिजली", "अस्पताल", "डॉक्टर", "पेंशन", "आधार", "पानी", "गैस", "ट्रेन", "मोबाइल"
        ]
        specific_enough = any(s in query_lower for s in specific_keywords)
        
        if matched_trigger and not specific_enough:
            q_text = item["question"].get(language, item["question"]["en"])
            return {
                "is_unclear": True,
                "question": q_text,
                "options": item["options"],
                "audio_text": sanitize_for_tts(q_text)
            }

    return None


def generate_task_guidance(query: str, language: str = "en") -> Dict[str, Any]:
    """
    Processes user request and returns complete structured step-by-step guidance.
    Prefers verified official service catalogs, falling back to Gemini reasoning or
    smart heuristic templates.
    """
    # Step 1: Check if query needs clarification first
    clarification = check_for_unclear_request(query, language=language)
    if clarification:
        return {
            "type": "CLARIFICATION",
            "data": clarification
        }

    # Step 2: Check verified service catalog
    matched_service = discover_online_service(query, language=language)
    if matched_service:
        # Pre-packaged verified guidance with full service metadata
        return {
            "type": "TASK",
            "task_id": matched_service["id"],
            "title": matched_service["title"],
            "official_name": matched_service["official_name"],
            "category": matched_service.get("category", ""),
            "government_level": matched_service.get("government_level", ""),
            "department": matched_service.get("department", ""),
            "india_gov_reference": matched_service.get("india_gov_reference", ""),
            "url": matched_service["url"],
            "safety": matched_service["safety"],
            "description": matched_service["description"],
            "steps": matched_service["steps"],
            "current_step": 0
        }

    # Step 3: Use Gemini AI to reason and generate a customized safe task breakdown
    api_key = get_gemini_api_key()
    lang_name = SUPPORTED_LANGUAGES.get(language, SUPPORTED_LANGUAGES["en"])["gemini_name"]

    if api_key:
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=api_key)

            prompt = f"""
You are GuideFlow AI, an empathetic, senior-friendly voice and web assistant.
The senior citizen asks: "{query}"
Language: {lang_name}

Create a calm, step-by-step guide (4 to 5 simple steps) explaining how to complete this task online.
Requirements:
- Emphasize safety: never share passwords or bank OTPs.
- Keep each step clear, short, and free of technical jargon.
- Format strictly as valid JSON matching this structure:
{{
  "title": "Short title of the task",
  "url": "Official web address or https://google.com search link",
  "official_name": "Name of official service or department",
  "description": "1 sentence calm summary of what we will do",
  "steps": [
    {{
      "title": "Step 1 title",
      "action": "Clear description of what to click or enter",
      "tip": "Helpful tip for senior citizens",
      "simplified": "Ultra-simple explanation with an everyday analogy"
    }}
  ]
}}
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )

            task_data = json.loads(response.text)
            
            # Verify website safety
            target_url = task_data.get("url", "https://google.com")
            safety_info = verify_website_safety(target_url, language=language)

            return {
                "type": "TASK",
                "task_id": "custom_gemini_task",
                "title": task_data.get("title", query),
                "official_name": task_data.get("official_name", "Official Online Portal"),
                "url": target_url,
                "safety": safety_info,
                "description": task_data.get("description", "Step-by-step guidance for your request."),
                "steps": task_data.get("steps", []),
                "current_step": 0
            }

        except Exception as e:
            # Fallback to general assistance template
            pass

    # Heuristic General Assistance Fallback
    default_url = "https://www.india.gov.in"
    safety = verify_website_safety(default_url, language=language)

    if language == "te":
        title = f"{query} - దశలవారీ సహాయం"
        desc = "మేము మీకు దశలవారీగా సులభంగా అర్థమయ్యేలా సహాయం చేస్తాము."
        steps = [
            {
                "title": "అధికారిక వెబ్‌సైట్‌ను తెరవండి",
                "action": "సురక్షితమైన అధికారిక పోర్టల్‌ను తెరవడానికి లింక్‌పై క్లిక్ చేయండి.",
                "tip": "వెబ్‌సైట్ అడ్రస్‌లో 'gov.in' లేదా సురక్షితమైన గుర్తు ఉందో లేదో చూడండి.",
                "simplified": "మొదట వెబ్‌సైట్‌ను తెరవండి. మేము మీతోనే ఉంటాము."
            },
            {
                "title": "మీకు అవసరమైన సేవను ఎంచుకోండి",
                "action": "స్క్రీన్‌పై కనిపించే ప్రధాన మెనూ లేదా సెర్చ్ బాక్స్‌లో మీ సేవను ఎంచుకోండి.",
                "tip": "ఏవైనా సందేహాలుంటే ఆందోళన చెందవద్దు.",
                "simplified": "పేజీలో కనిపించే పెద్ద అక్షరాల బటన్‌ను నొక్కండి."
            },
            {
                "title": "మీ సమాచారాన్ని నమోదు చేయండి",
                "action": "అడిగిన వివరాలను నెమ్మదిగా టైప్ చేయండి.",
                "tip": "మీ పాస్‌వర్డ్ లేదా బ్యాంక్ OTP ఎవరితోనూ పంచుకోవద్దు.",
                "simplified": "మీ వివరాలను బాక్స్‌లలో రాయండి. మీ రహస్య నంబర్లు ఎవరికీ చెప్పవద్దు."
            },
            {
                "title": "వివరాలను ధృవీకరించండి మరియు ముగించండి",
                "action": "నమోదు చేసిన వివరాలను మరోసారి చూసుకుని సబ్మిట్ చేయండి.",
                "tip": "రిఫరెన్స్ నంబర్‌ను ఒక కాగితంపై రాసి పెట్టుకోండి.",
                "simplified": "అంతా సరిగ్గా ఉందో చూసి పూర్తి చేయండి. మీ పని పూర్తయింది!"
            }
        ]
    elif language == "hi":
        title = f"{query} - चरण-दर-चरण मार्गदर्शन"
        desc = "हम आपको इस कार्य को पूरा करने के लिए सरल मार्गदर्शन प्रदान करेंगे।"
        steps = [
            {
                "title": "आधिकारिक वेबसाइट खोलें",
                "action": "सुरक्षित आधिकारिक पोर्टल खोलने के लिए लिंक पर क्लिक करें।",
                "tip": "वेबसाइट पते के अंत में '.gov.in' या सुरक्षित पैडलॉक चिह्न अवश्य देखें।",
                "simplified": "सबसे पहले वेबसाइट लिंक खोलें। हम आपके साथ हैं।"
            },
            {
                "title": "अपनी आवश्यक सेवा चुनें",
                "action": "स्क्रीन पर दिखने वाले मुख्य विकल्पों में से अपनी सेवा का चयन करें।",
                "tip": "यदि कोई विकल्प समझ न आए तो परेशान न हों।",
                "simplified": "स्क्रीन पर बड़े अक्षरों वाले विकल्प पर क्लिक करें।"
            },
            {
                "title": "अपनी जानकारी दर्ज करें",
                "action": "पूछी गई जानकारी को ध्यानपूर्वक भरें।",
                "tip": "अपना बैंक ओटीपी या पासवर्ड कभी किसी के साथ साझा न करें।",
                "simplified": "बॉक्स में मांगी गई जानकारी भरें। अपनी गोपनीय जानकारी सुरक्षित रखें।"
            },
            {
                "title": "जांचें और कार्य पूरा करें",
                "action": "जानकारी की पुष्टि करें और सबमिट बटन दबाएं।",
                "tip": "पुष्टि पर्ची या संदर्भ संख्या को नोट कर लें।",
                "simplified": "सब कुछ ठीक होने पर पूरा करें। आपका काम संपन्न हो गया!"
            }
        ]
    else:
        title = f"{query} - Step-by-Step Guidance"
        desc = "GuideFlow will walk you through completing this service safely and calmly."
        steps = [
            {
                "title": "Open the official portal",
                "action": "Click the safe link provided above to reach the verified service.",
                "tip": "Verify that the website uses HTTPS and trusted credentials.",
                "simplified": "Click the blue button to open the page. We will guide you from here."
            },
            {
                "title": "Locate your service",
                "action": "Look for the main service heading or category on the homepage.",
                "tip": "Do not click on third-party advertisements or pop-up boxes.",
                "simplified": "Look at the main menu and click the service name."
            },
            {
                "title": "Enter your information",
                "action": "Type in your required account number or identification details.",
                "tip": "Never enter your bank PIN or share an OTP with anyone.",
                "simplified": "Fill in the required box. Keep your private passwords safe."
            },
            {
                "title": "Review and confirm",
                "action": "Check that the summary details match your records before clicking Submit.",
                "tip": "Note down the acknowledgement or reference number.",
                "simplified": "Check everything one last time and submit. Your task is complete!"
            }
        ]

    return {
        "type": "TASK",
        "task_id": "general_guidance",
        "title": title,
        "official_name": "Official Citizen Service",
        "url": default_url,
        "safety": safety,
        "description": desc,
        "steps": steps,
        "current_step": 0
    }


def simplify_step_explanation(step: Dict[str, Any], language: str = "en") -> Dict[str, str]:
    """
    Triggered when the user clicks or says 'I don't understand'.
    Never repeats the exact same sentence.
    Breaks down the step into even simpler language, everyday metaphors,
    and physical visual pointers.
    """
    existing_simple = step.get("simplified", "")
    title = step.get("title", "")
    action = step.get("action", "")

    api_key = get_gemini_api_key()
    lang_name = SUPPORTED_LANGUAGES.get(language, SUPPORTED_LANGUAGES["en"])["gemini_name"]

    if api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            prompt = f"""
The senior citizen says "I don't understand" for this step:
Title: {title}
Original action: {action}
Language: {lang_name}

Provide an even simpler, crystal-clear explanation for an elderly person.
Rules:
- DO NOT repeat the original sentence.
- Use everyday words, physical landmarks (e.g. "Look for the large blue box at the top right"), and simple analogies.
- Keep it under 2 or 3 short, reassuring sentences.
- Respond directly in {lang_name}.
"""
            resp = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            simpler_text = resp.text.strip()
            return {
                "simpler_text": simpler_text,
                "audio_text": sanitize_for_tts(simpler_text)
            }
        except Exception:
            pass

    # High quality fallback simplification
    if language == "te":
        simpler_text = (
            f"ఆందోళన చెందకండి. దీని అర్థం చాలా సులభం: {existing_simple if existing_simple else 'మీ స్క్రీన్ మధ్యలో కనిపించే పెద్ద బటన్‌ను మాత్రమే నొక్కండి.'} "
            "మీరు ఏ తప్పు చేయరు, మేము మీకు సహాయంగా ఉన్నాము."
        )
    elif language == "hi":
        simpler_text = (
            f"चिंता मत कीजिए। इसका सरल अर्थ है: {existing_simple if existing_simple else 'अपनी स्क्रीन के मुख्य हिस्से पर बड़े बटन को देखें और उस पर क्लिक करें।'} "
            "आपसे कोई गलती नहीं होगी, हम आपके साथ हैं।"
        )
    else:
        simpler_text = (
            f"Don't worry at all. Here is an easier way to look at it: "
            f"{existing_simple if existing_simple else 'Just look for the large button in the center of the page.'} "
            "Take your time, you are doing great."
        )

    return {
        "simpler_text": simpler_text,
        "audio_text": sanitize_for_tts(simpler_text)
    }
