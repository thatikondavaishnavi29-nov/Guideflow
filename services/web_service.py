"""
GuideFlow AI - Official Indian Government Service Discovery Engine
Provides high-accuracy, explainable relevance scoring for official Indian government services.
Strictly maps citizen inquiries to verified portals from the National Portal of India (india.gov.in).
Never returns unrelated services (e.g., hospital for scholarship) or unverified third-party websites.
"""

import re
from typing import Dict, Any, List, Optional, Tuple

from services.gov_catalogue import (
    GOVERNMENT_SERVICES_CATALOGUE,
    OFFICIAL_GOV_CATEGORIES,
    get_catalogue,
    get_service_by_id,
    get_services_by_category
)
from services.safety_service import verify_website_safety

# Re-export catalogue for compatibility
VERIFIED_SERVICES_CATALOG = GOVERNMENT_SERVICES_CATALOGUE


def normalize_text(text: str) -> str:
    """Normalize text by converting to lowercase and stripping excess whitespace/punctuation."""
    if not text:
        return ""
    # Lowercase and replace common punctuation with spaces
    cleaned = re.sub(r'[,.?!/\\;:\'\"()\[\]{}_-]', ' ', text.lower())
    return ' '.join(cleaned.split())


def extract_tokens(text: str) -> List[str]:
    """Tokenize query into individual words, ignoring trivial stopwords."""
    stopwords = {"i", "want", "to", "need", "help", "me", "how", "can", "for", "a", "an", "the",
                 "in", "my", "online", "portal", "website", "get", "apply", "check", "find",
                 "నన్ను", "నాకు", "ఎలా", "చేయాలి", "కావాలి", "मुझे", "करना", "है", "के", "लिए", "का", "की"}
    norm = normalize_text(text)
    tokens = [t for t in norm.split() if len(t) > 1 and t not in stopwords]
    return tokens


def detect_target_categories(query: str) -> List[str]:
    """
    Identifies if a natural language query strongly targets a specific
    National Portal of India category based on high-signal trigger terms.
    """
    norm = normalize_text(query)
    targets = []

    # Category triggers
    triggers = {
        "Education & Learning": [
            "scholarship", "scholarships", "student", "college", "school", "fellowship",
            "stipend", "education", "study", "exam", "university",
            "స్కాలర్‌షిప్", "విద్యార్థి", "కాలేజీ", "వేతనం", "చదువు",
            "छात्रवृत्ति", "स्कॉलरशिप", "विद्यार्थी", "कॉलेज", "पढ़ाई", "वजीफा"
        ],
        "Citizenship, Visa & Passports": [
            "passport", "passports", "visa", "aadhaar", "aadhar", "voter", "epic",
            "citizenship", "uidai", "myaadhaar",
            "పాస్‌పోర్ట్", "ఆధార్", "ఓటరు", "ఎన్నిక",
            "पासपोर्ट", "आधार", "वोटर", "मतदाता", "पहचान पत्र"
        ],
        "Driving & Transport": [
            "driving", "licence", "license", "learner", "llr", "dl", "parivahan",
            "sarathi", "vehicle", "rto",
            "డ్రైవింగ్", "లైసెన్స్", "సారథి", "వాహనం",
            "ड्राइविंग", "लाइसेंस", "सारथी", "गाड़ी", "परिवहन"
        ],
        "Benefits & Social Development": [
            "ration", "food card", "nfsa", "pds", "caste certificate", "community certificate",
            "income certificate", "bpl", "annavitran", "sc st obc",
            "రేషన్", "ఆహార కార్డు", "కుల ధృవీకరణ", "ఆదాయ ధృవీకరణ",
            "राशन", "खाद्य", "जाति प्रमाण पत्र", "आय प्रमाण पत्र"
        ],
        "Housing & Local Services": [
            "birth certificate", "electricity", "power bill", "current bill", "bijli",
            "water bill", "property tax", "municipal", "crs",
            "జనన ధృవీకరణ", "కరెంట్ బిల్లు", "విద్యుత్", "మున్సిపల్",
            "जन्म प्रमाण पत्र", "बिजली", "विद्युत", "नगर पालिका"
        ],
        "Health & Wellness": [
            "hospital", "doctor", "appointment", "clinic", "health", "opd", "aiims",
            "patient", "medical", "treatment", "medicine",
            "ఆసుపత్రి", "డాక్టర్", "వైద్య", "ఆరోగ్య", "ఓపీడీ",
            "अस्पताल", "डॉक्टर", "दवाखाना", "स्वास्थ्य", "चिकित्सा", "ओपीडी"
        ],
        "Welfare of Families": [
            "pension", "jeevan pramaan", "life certificate", "senior citizen", "widow pension",
            "disability pension", "nsap",
            "పెన్షన్", "వృద్ధాప్య", "జీవన్ ప్రమాణ్", "లైఫ్ సర్టిఫికేట్",
            "पेंशन", "वृद्धावस्था", "जीवन प्रमाण", "वरिष्ठ नागरिक"
        ],
        "Jobs": [
            "job", "jobs", "government job", "career", "employment", "recruitment", "vacancy", "ncs",
            "ఉద్యోగం", "ఉద్యోగాలు", "ఉపాధి", "నియామకం",
            "नौकरी", "सरकारी नौकरी", "रोजगार", "भर्ती"
        ],
        "Money & Taxes": [
            "pan", "pan card", "income tax", "pf", "epfo", "provident fund", "uan", "tax return",
            "ప్యాన్", "పాన్ కార్డు", "ఆదాయపు పన్ను", "పీఎఫ్", "భవిష్య నిధి",
            "पैन", "पैन कार्ड", "आयकर", "पीएफ", "भविष्य निधि"
        ],
        "Agriculture, Rural & Environment": [
            "farmer", "kisan", "pm kisan", "agriculture", "land records", "bhulekh",
            "patta", "khasra", "ror",
            "రైతు", "పీఎం కిసాన్", "వ్యవసాయం", "భూ రికార్డులు", "పట్టా", "భూలేఖ్",
            "किसान", "पीएम किसान", "खेती", "भूलेख", "खसरा", "जमीन"
        ],
        "Justice, Law & Grievances": [
            "grievance", "complaint", "pg portal", "cpgrams", "darpg", "consumer court",
            "ఫిర్యాదు", "ప్రజా ఫిర్యాదు", "కంప్లైంట్",
            "शिकायत", "लोक शिकायत", "पीजी पोर्टल", "सीपीजीआरएएमएस"
        ]
    }

    # Whole-word token set for single-word trigger comparison
    norm_tokens = set(norm.split())

    for cat_name, keywords in triggers.items():
        matched = False
        for kw in keywords:
            kw_norm = normalize_text(kw)
            if not kw_norm:
                continue
            if " " in kw_norm:
                # Multi-word trigger: substring match is fine (must appear as a phrase)
                if kw_norm in norm:
                    matched = True
                    break
            else:
                # Single-word trigger: whole-word match only — prevents e.g. 'ration' in 'registration'
                if kw_norm in norm_tokens:
                    matched = True
                    break
        if matched:
            targets.append(cat_name)

    return targets



def calculate_relevance_score(query: str, service: Dict[str, Any]) -> float:
    """
    Computes a transparent relevance score between a user query and a government service.
    
    Scoring breakdown:
    - Negative keyword hit: -1000 (Hard instant disqualification)
    - Unrelated category penalty: -200
    - Exact service name match: +100
    - Exact alias match: +85
    - Partial/contained alias match: +60
    - Multi-word keyword match: +40
    - Token overlap match: +12 per token
    - Target category alignment: +35
    """
    norm_query = normalize_text(query)
    query_tokens = set(extract_tokens(query))
    
    if not norm_query:
        return 0.0

    score = 0.0

    # 1. HARD RULE: Negative Keywords Check
    # If the service explicitly specifies that it should NEVER match this term
    # (e.g. Hospital must NEVER match "scholarship", "driving", "passport")
    # IMPORTANT: Use whole-word (token-level) matching to prevent false hits.
    # e.g. negative keyword "ration" must NOT fire on query "registration"
    # because "ration" appears as a *substring* of "registration".
    neg_tokens = set(query_tokens)  # whole-word tokens from the actual query
    for neg_kw in service.get("negative_keywords", []):
        neg_kw_tokens = set(extract_tokens(neg_kw))
        if not neg_kw_tokens:
            continue
        # Multi-word negative keyword: require all its tokens to appear in query as a substring
        if " " in normalize_text(neg_kw):
            neg_norm = normalize_text(neg_kw)
            if neg_norm in norm_query:
                return -1000.0
        else:
            # Single-word negative keyword: must match as a complete word/token, NOT as substring
            if neg_kw_tokens.issubset(neg_tokens):
                return -1000.0

    # 2. Category Alignment & Cross-Category Penalty
    target_categories = detect_target_categories(query)
    service_cat = service.get("category", "")
    
    if target_categories:
        if service_cat in target_categories:
            score += 35.0
        else:
            # Strong penalty for services outside the targeted category
            score -= 200.0

    # 3. Match against Service Name (English, Telugu, Hindi)
    service_names = service.get("service_name", {})
    for lang, name in service_names.items():
        norm_name = normalize_text(name)
        if norm_name:
            if norm_query == norm_name:
                score += 100.0
            elif norm_name in norm_query or norm_query in norm_name:
                score += 75.0

    # 4. Match against Aliases
    aliases = service.get("aliases", [])
    for alias in aliases:
        norm_alias = normalize_text(alias)
        if norm_alias:
            if norm_query == norm_alias:
                score += 85.0
            elif norm_alias in norm_query:
                score += 65.0
            elif norm_query in norm_alias and len(norm_query) > 3:
                score += 45.0

    # 5. Multi-Word Keyword Matching
    keywords = service.get("keywords", [])
    for kw in keywords:
        norm_kw = normalize_text(kw)
        if norm_kw:
            if " " in norm_kw:  # Multi-word keyword phrase
                if norm_kw in norm_query:
                    score += 45.0
            else:  # Single token keyword
                if norm_kw in query_tokens:
                    score += 15.0

        # 6. Token Overlap Scoring
        service_text_blob = " ".join([
        " ".join(service.get("aliases", [])),
        " ".join(service.get("keywords", [])),
        service.get("category", "")
    ])

    service_tokens = set(extract_tokens(service_text_blob))

    overlap_count = sum(
        1 for token in query_tokens
        if token in service_tokens
    )

    score += overlap_count * 10.0

    if overlap_count >= 2:
            score += 20.0  # Bonus for multiple keyword hits

    return score


def search_government_services(query: str, language: str = "en") -> Dict[str, Any]:
    """
    Searches the official government catalogue for the given query.
    Returns:
    - match_type: 'EXACT', 'CLARIFICATION', or 'NONE'
    - service: Top matched service dictionary (or None)
    - candidates: Ranked list of top services with scores
    - category: The targeted official India.gov.in category
    """
    if not query or not query.strip():
        return {
            "match_type": "NONE",
            "service": None,
            "candidates": [],
            "category": None
        }

    catalogue = get_catalogue()
    scored_services: List[Tuple[float, Dict[str, Any]]] = []

    for s in catalogue:
        s_score = calculate_relevance_score(query, s)
        if s_score > 0:
            scored_services.append((s_score, s))

    # Sort descending by relevance score
    scored_services.sort(key=lambda x: x[0], reverse=True)

    if not scored_services:
        return {
            "match_type": "NONE",
            "service": None,
            "candidates": [],
            "category": None
        }

    top_score, top_service = scored_services[0]

    # Evaluate confidence threshold
    # If the score is high and clearly beats the runner-up
    if top_score >= 50.0:
        # Check runner-up
        if len(scored_services) > 1:
            runner_score, runner_service = scored_services[1]
            # If the runner-up is from the same category with a very close score
            if (top_score - runner_score) < 15.0 and runner_service["category"] == top_service["category"]:
                # Ambiguous query within the same category (e.g. user just said "certificate" or "scheme")
                return {
                    "match_type": "CLARIFICATION",
                    "service": top_service,
                    "candidates": [s for _, s in scored_services[:3]],
                    "category": top_service["category"]
                }

        # Clear high-confidence exact match
        return {
            "match_type": "EXACT",
            "service": top_service,
            "candidates": [s for _, s in scored_services[:3]],
            "category": top_service["category"]
        }

    # Medium or low score -> Ask for clarification within candidate services
    if top_score >= 25.0:
        return {
            "match_type": "CLARIFICATION",
            "service": top_service,
            "candidates": [s for _, s in scored_services[:3]],
            "category": top_service["category"]
        }

    return {
        "match_type": "NONE",
        "service": None,
        "candidates": [],
        "category": None
    }


def discover_online_service(query: str, language: str = "en") -> Optional[Dict[str, Any]]:
    """
    Main interface for discovering verified government services.
    Returns full guidance data along with safety verification from the National Portal catalogue.
    """
    search_res = search_government_services(query, language=language)

    # If exact match or top candidate with high score
    if search_res["match_type"] in ["EXACT", "CLARIFICATION"] and search_res["service"]:
        best = search_res["service"]
        
        # Verify target URL safety
        safety = verify_website_safety(best["official_url"], language=language)
        
        # Localize service title and description
        title = best["service_name"].get(language, best["service_name"]["en"])
        desc = best["description"].get(language, best["description"]["en"])

        return {
            "id": best["service_id"],
            "title": title,
            "official_name": f"{best['department']} ({best['government_level']} Government)",
            "category": best["category"],
            "government_level": best["government_level"],
            "department": best["department"],
            "url": best["official_url"],
            "india_gov_reference": best.get("india_gov_reference", "https://www.india.gov.in/"),
            "safety": safety,
            "description": desc,
            "required_items": best.get("required_items", ["Aadhaar or Identity Proof"]),
            "steps": best.get("typical_steps", [])
        }

    return None
