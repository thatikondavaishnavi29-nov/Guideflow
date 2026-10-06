"""
GuideFlow AI - Privacy and Sensitive Information Protection
Detects, masks, and protects sensitive user data (Aadhaar, PAN, Cards, Phone, OTPs, Passwords).
Ensures sensitive details are NEVER spoken aloud by Text-to-Speech engines.
"""

import re
from typing import List, Dict, Tuple, Any

# Compiled regex patterns for privacy detection
PATTERNS = {
    "aadhaar": re.compile(r'\b[2-9]\d{3}[\s\-]?\d{4}[\s\-]?\d{4}\b(?!\s?[\d])'),
    "pan_card": re.compile(r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b', re.IGNORECASE),
    "credit_card": re.compile(r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13})\b|\b(?:\d{4}[\s\-]){3}\d{4}\b'),
    "phone_number": re.compile(r'(?:\+91[\s\-]?)?[6-9]\d{9}\b'),
    "otp_code": re.compile(r'(?:otp|one\s*time\s*password|verification\s*code|pin)[\s\:\-=#]*(?:is[\s\:]*)?(\d{4,6})\b', re.IGNORECASE),
    "password": re.compile(r'(?:password|passcode|secret\s*key)[\s\:\-=#]+([^\s,;]+)', re.IGNORECASE),
    "cvv": re.compile(r'\b(?:cvv|cvc|security\s*code)[\s\:\-=#]+(\d{3,4})\b', re.IGNORECASE)
}


def detect_sensitive_info(text: str) -> List[Dict[str, Any]]:
    """
    Scans text and returns a list of detected sensitive information items.
    """
    if not text:
        return []
        
    findings = []
    
    # Aadhaar detection
    for match in PATTERNS["aadhaar"].finditer(text):
        digits = re.sub(r'[\s\-]', '', match.group(0))
        if len(digits) == 12:
            findings.append({
                "type": "Aadhaar Number",
                "matched": match.group(0),
                "safe_replacement": f"XXXX-XXXX-{digits[-4:]}",
                "severity": "HIGH",
                "start": match.start(),
                "end": match.end()
            })

    # PAN Card
    for match in PATTERNS["pan_card"].finditer(text):
        pan = match.group(0).upper()
        findings.append({
            "type": "PAN Card Number",
            "matched": match.group(0),
            "safe_replacement": f"XXXXX{pan[5:9]}X",
            "severity": "MEDIUM",
            "start": match.start(),
            "end": match.end()
        })

    # Credit/Debit Card
    for match in PATTERNS["credit_card"].finditer(text):
        digits = re.sub(r'[\s\-]', '', match.group(0))
        findings.append({
            "type": "Credit/Debit Card",
            "matched": match.group(0),
            "safe_replacement": f"XXXX-XXXX-XXXX-{digits[-4:]}",
            "severity": "CRITICAL",
            "start": match.start(),
            "end": match.end()
        })

    # OTP Code
    for match in PATTERNS["otp_code"].finditer(text):
        code = match.group(1)
        findings.append({
            "type": "One-Time Password (OTP)",
            "matched": match.group(0),
            "safe_replacement": match.group(0).replace(code, "[OTP PROTECTED]"),
            "severity": "CRITICAL",
            "start": match.start(),
            "end": match.end()
        })

    # CVV
    for match in PATTERNS["cvv"].finditer(text):
        cvv = match.group(1)
        findings.append({
            "type": "Card CVV",
            "matched": match.group(0),
            "safe_replacement": match.group(0).replace(cvv, "***"),
            "severity": "CRITICAL",
            "start": match.start(),
            "end": match.end()
        })

    # Password
    for match in PATTERNS["password"].finditer(text):
        pwd = match.group(1)
        findings.append({
            "type": "Password",
            "matched": match.group(0),
            "safe_replacement": match.group(0).replace(pwd, "[SECRET PROTECTED]"),
            "severity": "CRITICAL",
            "start": match.start(),
            "end": match.end()
        })

    # Mobile Phone
    for match in PATTERNS["phone_number"].finditer(text):
        raw = match.group(0)
        digits = re.sub(r'\D', '', raw)
        # Avoid double-tagging credit card or aadhaar numbers
        if len(digits) == 10:
            findings.append({
                "type": "Phone Number",
                "matched": raw,
                "safe_replacement": f"XXXXXX{digits[-4:]}",
                "severity": "LOW",
                "start": match.start(),
                "end": match.end()
            })

    return findings


def redact_sensitive_text(text: str) -> str:
    """
    Replaces all sensitive occurrences in the text with safe masked representations.
    """
    if not text:
        return text

    redacted = text

    # Redact Aadhaar
    redacted = PATTERNS["aadhaar"].sub(
        lambda m: f"XXXX-XXXX-{re.sub(r'[^0-9]', '', m.group(0))[-4:]}", 
        redacted
    )

    # Redact Credit/Debit Card
    redacted = PATTERNS["credit_card"].sub(
        lambda m: f"XXXX-XXXX-XXXX-{re.sub(r'[^0-9]', '', m.group(0))[-4:]}", 
        redacted
    )

    # Redact PAN
    redacted = PATTERNS["pan_card"].sub(
        lambda m: f"{m.group(0)[:2]}XXX{m.group(0)[-2:]}", 
        redacted
    )

    # Redact OTP
    redacted = PATTERNS["otp_code"].sub(
        lambda m: m.group(0).replace(m.group(1), "[OTP REDACTED]"), 
        redacted
    )

    # Redact CVV
    redacted = PATTERNS["cvv"].sub(
        lambda m: m.group(0).replace(m.group(1), "***"), 
        redacted
    )

    # Redact Password
    redacted = PATTERNS["password"].sub(
        lambda m: m.group(0).replace(m.group(1), "[PROTECTED]"), 
        redacted
    )

    return redacted


def sanitize_for_tts(text: str) -> str:
    """
    Prepares text specifically for Text-To-Speech audio output.
    Ensures that sensitive information like Aadhaar, card numbers, OTPs,
    and passwords are NEVER read aloud through the speaker.
    """
    if not text:
        return ""

    tts_clean = text

    # Replace Card numbers first (16 digits)
    tts_clean = PATTERNS["credit_card"].sub("your card ending in four digits", tts_clean)

    # Replace Aadhaar numbers (12 digits)
    tts_clean = PATTERNS["aadhaar"].sub("your Aadhaar number ending in four digits", tts_clean)

    # Replace PAN numbers
    tts_clean = PATTERNS["pan_card"].sub("your PAN number", tts_clean)

    # Replace OTPs
    tts_clean = PATTERNS["otp_code"].sub("your verification code", tts_clean)

    # Replace Phone numbers
    tts_clean = PATTERNS["phone_number"].sub("your phone number ending in four digits", tts_clean)

    # Replace CVV
    tts_clean = PATTERNS["cvv"].sub("your card security code", tts_clean)

    # Replace Passwords
    tts_clean = PATTERNS["password"].sub("your password", tts_clean)

    # Remove code blocks or raw JSON symbols if any appear in text
    tts_clean = re.sub(r'[`*#_>\[\]]', ' ', tts_clean)
    tts_clean = re.sub(r'\s+', ' ', tts_clean).strip()

    return tts_clean
