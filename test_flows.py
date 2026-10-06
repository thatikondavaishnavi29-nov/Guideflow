"""
GuideFlow AI - Comprehensive Automated Verification Test Suite
Tests all 8 mandatory flows specified in the product requirements:
1. Text Query ('How can I pay my electricity bill?')
2. Voice Query ('I want to book a hospital appointment')
3. Screenshot & Visual Understanding
4. 'I don't understand' Simplification
5. Multilingual Support (English, Telugu, Hindi)
6. Sensitive Information Redaction & Audio Sanitization
7. Unsafe / Suspicious Website Warning
8. Voice Commands ('Next', 'Back', 'Repeat', 'I don't understand', 'Stop')
"""

import os
import sys
import io
from PIL import Image, ImageDraw, ImageFont

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Ensure Windows terminal outputs Unicode cleanly
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from services.ai_service import generate_task_guidance, simplify_step_explanation, check_for_unclear_request
from services.speech_service import generate_tts_audio, transcribe_audio_bytes
from services.vision_service import analyze_image_input
from services.safety_service import verify_website_safety
from services.memory_service import load_memory, save_memory, clear_memory
from utils.privacy import detect_sensitive_info, redact_sensitive_text, sanitize_for_tts
from utils.helpers import parse_voice_command, get_text


def test_1_text_query():
    print("\n--- TEST 1: Text Query ('How can I pay my electricity bill?') ---")
    query = "How can I pay my electricity bill?"
    result = generate_task_guidance(query, language="en")
    
    assert result["type"] == "TASK", f"Expected type TASK, got {result.get('type')}"
    assert "Electricity" in result["title"] or "Bill" in result["title"], f"Unexpected title: {result['title']}"
    assert len(result["steps"]) >= 4, f"Expected at least 4 steps, got {len(result['steps'])}"
    assert result["safety"]["status"] == "VERIFIED", f"Expected VERIFIED, got {result['safety']['status']}"
    print(f"✅ Understood Intent: {result['title']}")
    print(f"✅ Verified Website Found: {result['url']} ({result['safety']['badge']})")
    print(f"✅ Steps Count: {len(result['steps'])}")
    for i, step in enumerate(result["steps"]):
        print(f"   Step {i+1}: {step['title']}")


def test_2_voice_query():
    print("\n--- TEST 2: Voice Query Simulation ('I want to book a hospital appointment.') ---")
    query = "I want to book a hospital appointment."
    
    # 1. Intent understanding & Task guidance
    result = generate_task_guidance(query, language="en")
    assert result["type"] == "TASK", "Failed to identify hospital task"
    assert "Hospital" in result["title"] or "Doctor" in result["title"]
    print(f"✅ Voice Intent Understood: {result['title']}")
    
    # 2. Voice response synthesis (TTS)
    voice_resp = f"I will guide you to book your hospital appointment step by step."
    audio = generate_tts_audio(voice_resp, language="en")
    assert audio is not None and len(audio) > 1000, "TTS audio generation failed"
    print(f"✅ Audio Synthesized Successfully ({len(audio)} bytes)")


def test_3_screenshot_analysis():
    print("\n--- TEST 3: Screenshot Analysis ---")
    # Create a simulated webpage screenshot image in memory
    img = Image.new("RGB", (600, 400), color=(240, 245, 250))
    d = ImageDraw.Draw(img)
    d.rectangle([(20, 20), (580, 80)], fill=(13, 148, 136))
    d.text((40, 40), "Official Utility Bill Payment Portal", fill=(255, 255, 255))
    d.rectangle([(40, 120), (500, 180)], outline=(100, 116, 139), width=2)
    d.text((50, 140), "Enter Consumer Number: 1029384756", fill=(30, 41, 59))
    d.rectangle([(40, 220), (220, 270)], fill=(2, 132, 199))
    d.text((60, 235), "PROCEED", fill=(255, 255, 255))

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    img_bytes = buf.getvalue()

    analysis = analyze_image_input(img_bytes, language="en")
    assert analysis["success"] is True, "Image analysis failed"
    assert len(analysis["summary"]) > 10, "Summary was empty"
    assert len(analysis["action"]) > 5, "Action was empty"
    print(f"✅ Analysis Summary: {analysis['summary'][:100]}...")
    print(f"✅ Action Recommended: {analysis['action']}")
    print(f"✅ Identified Elements: {analysis['elements']}")


def test_4_dont_understand_simplification():
    print("\n--- TEST 4: 'I don't understand' Simplification ---")
    complex_step = {
        "title": "Authenticate using your registered consumer credentials and dual factor authentication",
        "action": "Input your credentials into the multi-factor authentication prompt.",
        "tip": "Ensure OTP matches mobile SMS.",
        "simplified": "Enter the mobile number that you used when you created this account."
    }

    simplified = simplify_step_explanation(complex_step, language="en")
    simpler_text = simplified["simpler_text"]

    # Verify rule: DO NOT simply repeat the exact same sentence
    assert simpler_text != complex_step["action"], "Simplification merely repeated the original sentence!"
    assert "account" in simpler_text or "number" in simpler_text or "worry" in simpler_text or "mobile" in simpler_text
    print(f"✅ Original Step: {complex_step['action']}")
    print(f"✅ Simplified Explanation: {simpler_text}")
    print(f"✅ Sanitized for Voice Audio: {simplified['audio_text'][:60]}...")


def test_5_multilingual():
    print("\n--- TEST 5: Multilingual Support (English, Telugu, Hindi) ---")
    languages = [
        ("en", "How can I pay electricity bill?", "Electricity Bill Payment"),
        ("te", "కరెంట్ బిల్లు ఎలా చెల్లించాలి?", "విద్యుత్ బిల్లు చెల్లింపు"),
        ("hi", "बिजली का बिल कैसे भरें?", "बिजली बिल भुगतान")
    ]

    for lang_code, sample_query, expected_phrase in languages:
        guidance = generate_task_guidance(sample_query, language=lang_code)
        assert guidance["type"] == "TASK", f"Failed task generation for {lang_code}"
        
        # Test TTS for each language
        tts_audio = generate_tts_audio(guidance["title"], language=lang_code)
        assert tts_audio is not None and len(tts_audio) > 500, f"TTS audio failed for {lang_code}"
        
        # Test UI translation string
        ui_btn = get_text("btn_next", lang=lang_code)
        
        print(f"✅ Language: {lang_code.upper()}")
        print(f"   Task Title: {guidance['title']}")
        print(f"   Next Button Label: {ui_btn}")
        print(f"   TTS Audio Bytes: {len(tts_audio)} bytes generated successfully")


def test_6_sensitive_information():
    print("\n--- TEST 6: Sensitive Information Redaction & Audio Sanitization ---")
    sample_text = (
        "Customer Aadhaar: 9876 5432 1098, Phone: 9876543210, "
        "Card Number: 4111 2222 3333 4444, OTP is 654321, Password: SecretKey123"
    )

    findings = detect_sensitive_info(sample_text)
    assert len(findings) >= 4, f"Expected at least 4 sensitive items, found {len(findings)}"
    
    redacted = redact_sensitive_text(sample_text)
    # Check that raw full numbers are NOT in redacted text
    assert "9876 5432 1098" not in redacted
    assert "4111 2222 3333 4444" not in redacted
    assert "SecretKey123" not in redacted

    tts_clean = sanitize_for_tts(sample_text)
    # Check that numbers and passwords will NEVER be spoken aloud by TTS
    assert "9876 5432 1098" not in tts_clean
    assert "4111" not in tts_clean
    assert "654321" not in tts_clean
    assert "SecretKey123" not in tts_clean

    print(f"✅ Raw Text: {sample_text[:60]}...")
    print(f"✅ Redacted Output for Display: {redacted}")
    print(f"✅ Sanitized Text for Audio/TTS: {tts_clean}")
    print(f"✅ Total Sensitive Items Guarded: {len(findings)}")


def test_7_unsafe_website():
    print("\n--- TEST 7: Unsafe Website Scenario ---")
    safe_url = "https://myaadhaar.uidai.gov.in"
    suspicious_url = "http://fake-electricity-bill-pay.xyz/login.php"
    ip_url = "http://192.168.1.1/pay-now"

    # 1. Safe official website
    res_safe = verify_website_safety(safe_url, language="en")
    assert res_safe["status"] == "VERIFIED", "Failed to verify official UIDAI domain"
    assert res_safe["is_safe_to_open"] is True

    # 2. Suspicious TLD (.xyz)
    res_sus = verify_website_safety(suspicious_url, language="en")
    assert res_sus["status"] == "WARNING", "Failed to flag suspicious .xyz domain"
    assert res_sus["is_safe_to_open"] is False
    assert len(res_sus["voice_warning"]) > 10

    # 3. IP address URL
    res_ip = verify_website_safety(ip_url, language="en")
    assert res_ip["status"] == "WARNING", "Failed to flag raw IP URL"
    assert res_ip["is_safe_to_open"] is False

    print(f"✅ Safe Verified Portal ({safe_url}): {res_safe['status']} ({res_safe['badge']})")
    print(f"✅ Suspicious URL Blocked ({suspicious_url}): {res_sus['status']} ({res_sus['badge']})")
    print(f"   Voice Warning: \"{res_sus['voice_warning']}\"")
    print(f"✅ Raw IP Blocked ({ip_url}): {res_ip['status']}")


def test_8_voice_commands():
    print("\n--- TEST 8: Voice Commands across English, Telugu, and Hindi ---")
    commands_to_test = [
        # English
        ("next", "NEXT"),
        ("next step", "NEXT"),
        ("go back", "BACK"),
        ("repeat", "REPEAT"),
        ("i don't understand", "SIMPLIFY"),
        ("stop", "STOP"),
        # Telugu
        ("తరువాత", "NEXT"),
        ("వెనుక", "BACK"),
        ("మళ్లీ చెప్పండి", "REPEAT"),
        ("నాకు అర్థం కాలేదు", "SIMPLIFY"),
        ("ఆపు", "STOP"),
        # Hindi
        ("अगला कदम", "NEXT"),
        ("पीछे", "BACK"),
        ("दोहराएं", "REPEAT"),
        ("मुझे समझ नहीं आया", "SIMPLIFY"),
        ("रुको", "STOP")
    ]

    for phrase, expected_cmd in commands_to_test:
        parsed = parse_voice_command(phrase)
        assert parsed == expected_cmd, f"Command '{phrase}' parsed as '{parsed}', expected '{expected_cmd}'"
        print(f"✅ Spoken phrase '{phrase}' -> Action: {parsed}")


def run_all_tests():
    print("==================================================================")
    print("STARTING GUIDEFLOW AI COMPREHENSIVE VERIFICATION SUITE")
    print("==================================================================")
    
    test_1_text_query()
    test_2_voice_query()
    test_3_screenshot_analysis()
    test_4_dont_understand_simplification()
    test_5_multilingual()
    test_6_sensitive_information()
    test_7_unsafe_website()
    test_8_voice_commands()
    test_9_service_discovery_catalogue()

    print("\n==================================================================")
    print("🎉 ALL 9 MANDATORY VERIFICATION TESTS PASSED SUCCESSFULLY!")
    print("==================================================================")


def test_9_service_discovery_catalogue():
    """
    TEST 9 — Official Indian Government Service Discovery System
    Verifies that user queries reliably match the correct official service
    from the NPI-aligned catalogue, with no cross-category contamination.
    Covers all 19 service queries required in the product specification.
    """
    print("\n[TEST 9] Service Discovery Catalogue — 19 queries")

    from services.web_service import search_government_services

    # (query, expected_service_id, expected_category)
    service_tests = [
        ("scholarship",                     "nsp_scholarship",           "Education & Learning"),
        ("student scholarship",             "nsp_scholarship",           "Education & Learning"),
        ("I need financial help for college","nsp_scholarship",           "Education & Learning"),
        ("education scholarship",           "nsp_scholarship",           "Education & Learning"),
        ("passport",                        "passport_seva",             "Citizenship, Visa & Passports"),
        ("new passport application",        "passport_seva",             "Citizenship, Visa & Passports"),
        ("Aadhaar card download",           "myaadhaar_services",        "Citizenship, Visa & Passports"),
        ("PAN card",                        "pan_card_service",          "Money & Taxes"),
        ("voter ID",                        "voter_services",            "Citizenship, Visa & Passports"),
        ("voter card registration",         "voter_services",            "Citizenship, Visa & Passports"),
        ("driving licence",                 "driving_licence_sarathi",   "Driving & Transport"),
        ("I want a learner licence",        "driving_licence_sarathi",   "Driving & Transport"),
        ("ration card",                     "ration_card_nfsa",          "Benefits & Social Development"),
        ("I need a new ration card",        "ration_card_nfsa",          "Benefits & Social Development"),
        ("birth certificate",               "birth_certificate_crs",     "Housing & Local Services"),
        ("birth registration online",       "birth_certificate_crs",     "Housing & Local Services"),
        ("caste certificate",               "caste_certificate_service", "Benefits & Social Development"),
        ("income certificate",              "income_certificate_service","Benefits & Social Development"),
        ("pension",                         "pension_services",          "Welfare of Families"),
        ("old age pension",                 "pension_services",          "Welfare of Families"),
        ("jeevan pramaan life certificate", "pension_services",          "Welfare of Families"),
        ("government job",                  "national_career_service",   "Jobs"),
        ("job registration employment",     "national_career_service",   "Jobs"),
        ("PF balance EPFO",                 "epfo_pf_services",          "Money & Taxes"),
        ("provident fund withdrawal",       "epfo_pf_services",          "Money & Taxes"),
        ("electricity bill payment",        "electricity_bill_bbps",     "Housing & Local Services"),
        ("land records bhulekh",            "land_records_dilrmp",       "Agriculture, Rural & Environment"),
        ("farmer scheme PM Kisan",          "pm_kisan_samman",           "Agriculture, Rural & Environment"),
        ("hospital appointment",            "ors_hospital_appointment",  "Health & Wellness"),
        ("doctor consultation booking",     "ors_hospital_appointment",  "Health & Wellness"),
        ("grievance complaint government",  "cpgrams_grievance",         "Justice, Law & Grievances"),
    ]

    failures = []
    for query, exp_id, exp_cat in service_tests:
        result = search_government_services(query)
        svc = result.get("service")
        got_id  = svc["service_id"] if svc else "None"
        got_cat = result.get("category", "N/A") or "N/A"
        ok = (got_id == exp_id) and (got_cat == exp_cat)
        if not ok:
            failures.append((query, exp_id, exp_cat, got_id, got_cat))

    if failures:
        print("  FAILED QUERIES:")
        for q, ei, ec, gi, gc in failures:
            print(f"    QUERY: {q!r}")
            print(f"      Expected: {ei} ({ec})")
            print(f"      Got:      {gi} ({gc})")
        raise AssertionError(f"[TEST 9] {len(failures)} service discovery assertions failed")

    print(f"  ✅ All {len(service_tests)} service discovery queries matched correct official services")

    # Critical anti-regression: "scholarship" must NEVER return hospital/ORS
    scholarship_result = search_government_services("scholarship")
    svc = scholarship_result.get("service")
    if svc:
        assert svc["service_id"] != "ors_hospital_appointment", \
            "[TEST 9 CRITICAL] 'scholarship' returned ors_hospital_appointment — BUG REGRESSED!"
        assert svc["service_id"] == "nsp_scholarship", \
            f"[TEST 9 CRITICAL] 'scholarship' returned wrong service: {svc['service_id']}"
    print("  ✅ Critical anti-regression check passed (scholarship ≠ hospital)")
    print("[TEST 9] PASSED\n")


if __name__ == "__main__":
    run_all_tests()
