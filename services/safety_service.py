"""
GuideFlow AI - Website Safety & Trust Verification Service
Analyzes domains, URLs, and security indicators to protect senior citizens
from phishing, scams, unverified portals, and fraudulent web links.
"""

import re
import urllib.parse
from typing import Dict, Any, List

import tldextract
from utils.config import OFFICIAL_TRUSTED_DOMAINS, SUSPICIOUS_TLDS
from utils.helpers import get_text


def is_ip_address(host: str) -> bool:
    """Check if the hostname is a raw IP address."""
    ip_pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    return bool(re.match(ip_pattern, host))


def verify_website_safety(url: str, language: str = "en") -> Dict[str, Any]:
    """
    Verifies whether a given URL is a trusted official portal, safe public service,
    or potentially suspicious/unverified website.
    Returns clear senior-friendly guidance and warning strings.
    """
    if not url:
        return {
            "status": "UNKNOWN",
            "is_safe_to_open": False,
            "badge": "⚠️ Unknown",
            "title": "No Website Provided",
            "description": "No website link was provided to inspect.",
            "voice_warning": "",
            "risk_level": "MEDIUM"
        }

    # Normalize URL scheme
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urllib.parse.urlparse(url)
    hostname = parsed.hostname or ""
    scheme = parsed.scheme.lower()

    # Extract domain components using tldextract
    extracted = tldextract.extract(url)
    registered_domain = extracted.registered_domain.lower()
    suffix = extracted.suffix.lower()
    domain_name = extracted.domain.lower()

    # Check 1: Raw IP addresses are high risk
    if is_ip_address(hostname):
        warning_msg = get_text("safety_warning_msg", language)
        return {
            "status": "WARNING",
            "is_safe_to_open": False,
            "badge": "🚫 High Risk",
            "title": get_text("safety_warning_title", language),
            "description": "This link uses an IP number instead of a verified name. Official services never use IP addresses.",
            "voice_warning": warning_msg,
            "risk_level": "HIGH",
            "url": url
        }

    # Check 2: Suspicious TLD check (.xyz, .tk, .work, etc.)
    if suffix in SUSPICIOUS_TLDS:
        warning_msg = get_text("safety_warning_msg", language)
        return {
            "status": "WARNING",
            "is_safe_to_open": False,
            "badge": "⚠️ Suspicious Extension",
            "title": get_text("safety_warning_title", language),
            "description": f"The website ends with '.{suffix}', which is commonly linked to unverified or scam pages. Please do not enter passwords or bank details.",
            "voice_warning": warning_msg,
            "risk_level": "HIGH",
            "url": url
        }

    # Check 3: Whitelisted Official Trusted Domains
    is_official = False
    for trusted in OFFICIAL_TRUSTED_DOMAINS:
        if hostname == trusted or hostname.endswith("." + trusted):
            is_official = True
            break

    if is_official:
        verified_title = get_text("website_verified", language)
        return {
            "status": "VERIFIED",
            "is_safe_to_open": True,
            "badge": "🛡️ Verified Official",
            "title": verified_title,
            "description": f"This is a verified official portal ({registered_domain}). You can safely follow GuideFlow's steps here.",
            "voice_warning": "",
            "risk_level": "LOW",
            "url": url
        }

    # Check 4: General HTTPS website (legitimate reputable service, e.g. Amazon, Airtel, etc.)
    if scheme == "https":
        # Safe to open, but remind senior to stay cautious
        return {
            "status": "CAUTION",
            "is_safe_to_open": True,
            "badge": "ℹ️ Standard Service",
            "title": "Legitimate Online Service",
            "description": f"This is an online service at {registered_domain}. GuideFlow will guide you step-by-step. Remember: never share your OTP.",
            "voice_warning": "",
            "risk_level": "LOW",
            "url": url
        }

    # Check 5: Insecure HTTP (unencrypted)
    warning_msg = get_text("safety_warning_msg", language)
    return {
        "status": "WARNING",
        "is_safe_to_open": False,
        "badge": "⚠️ Insecure (Not Encrypted)",
        "title": get_text("safety_warning_title", language),
        "description": "This website is not encrypted (it does not use HTTPS). Your personal details could be intercepted.",
        "voice_warning": warning_msg,
        "risk_level": "MEDIUM",
        "url": url
    }
