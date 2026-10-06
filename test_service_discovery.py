"""
Quick service discovery smoke test - run this file directly.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from services.web_service import search_government_services

TESTS = [
    ("scholarship",                     "Education & Learning",             "nsp_scholarship"),
    ("student scholarship",             "Education & Learning",             "nsp_scholarship"),
    ("I need financial help for college","Education & Learning",             "nsp_scholarship"),
    ("education scholarship",           "Education & Learning",             "nsp_scholarship"),
    ("passport",                        "Citizenship, Visa & Passports",    "passport_seva"),
    ("new passport application",        "Citizenship, Visa & Passports",    "passport_seva"),
    ("I want to apply for passport",    "Citizenship, Visa & Passports",    "passport_seva"),
    ("Aadhaar card download",           "Citizenship, Visa & Passports",    "myaadhaar_services"),
    ("uidai portal",                    "Citizenship, Visa & Passports",    "myaadhaar_services"),
    ("PAN card",                        "Money & Taxes",                    "pan_card_service"),
    ("apply PAN card income tax",       "Money & Taxes",                    "pan_card_service"),
    ("voter ID",                        "Citizenship, Visa & Passports",    "voter_services"),
    ("voter card registration",         "Citizenship, Visa & Passports",    "voter_services"),
    ("driving licence",                 "Driving & Transport",              "driving_licence_sarathi"),
    ("I want a learner licence",        "Driving & Transport",              "driving_licence_sarathi"),
    ("driving license renewal",         "Driving & Transport",              "driving_licence_sarathi"),
    ("ration card",                     "Benefits & Social Development",    "ration_card_nfsa"),
    ("food card apply",                 "Benefits & Social Development",    "ration_card_nfsa"),
    ("I need a new ration card",        "Benefits & Social Development",    "ration_card_nfsa"),
    ("birth certificate",               "Housing & Local Services",         "birth_certificate_crs"),
    ("birth registration online",       "Housing & Local Services",         "birth_certificate_crs"),
    ("caste certificate",               "Benefits & Social Development",    "caste_certificate_service"),
    ("community certificate apply",     "Benefits & Social Development",    "caste_certificate_service"),
    ("income certificate",              "Benefits & Social Development",    "income_certificate_service"),
    ("annual income certificate online","Benefits & Social Development",    "income_certificate_service"),
    ("pension",                         "Welfare of Families",              "pension_services"),
    ("old age pension",                 "Welfare of Families",              "pension_services"),
    ("pension application",             "Welfare of Families",              "pension_services"),
    ("jeevan pramaan life certificate", "Welfare of Families",              "pension_services"),
    ("government job",                  "Jobs",                             "national_career_service"),
    ("job registration employment",     "Jobs",                             "national_career_service"),
    ("find government jobs",            "Jobs",                             "national_career_service"),
    ("PF balance EPFO",                 "Money & Taxes",                    "epfo_pf_services"),
    ("provident fund withdrawal",       "Money & Taxes",                    "epfo_pf_services"),
    ("electricity bill payment",        "Housing & Local Services",         "electricity_bill_bbps"),
    ("pay current bill",                "Housing & Local Services",         "electricity_bill_bbps"),
    ("land records bhulekh",            "Agriculture, Rural & Environment", "land_records_dilrmp"),
    ("patta khatauni land ownership",   "Agriculture, Rural & Environment", "land_records_dilrmp"),
    ("farmer scheme PM Kisan",          "Agriculture, Rural & Environment", "pm_kisan_samman"),
    ("kisan samman nidhi",              "Agriculture, Rural & Environment", "pm_kisan_samman"),
    ("hospital appointment",            "Health & Wellness",                "ors_hospital_appointment"),
    ("doctor consultation booking",     "Health & Wellness",                "ors_hospital_appointment"),
    ("online doctor appointment",       "Health & Wellness",                "ors_hospital_appointment"),
    ("grievance complaint government",  "Justice, Law & Grievances",        "cpgrams_grievance"),
    ("file complaint government",       "Justice, Law & Grievances",        "cpgrams_grievance"),
]

def run_tests():
    print("="*72)
    print("SERVICE DISCOVERY ENGINE - COMPREHENSIVE TEST SUITE")
    print("="*72)
    passed = 0
    failed = 0
    failures = []
    for query, exp_cat, exp_id in TESTS:
        r = search_government_services(query)
        svc = r.get('service')
        got_cat = r.get('category', 'N/A') or 'N/A'
        got_id  = svc['service_id'] if svc else 'None'
        match_type = r.get('match_type', 'NONE')
        ok = (got_cat == exp_cat) and (got_id == exp_id)
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
            failures.append((query, exp_cat, exp_id, got_cat, got_id, match_type))
        print(f"[{status}] \"{query}\"")
        if not ok:
            print(f"       Expected: {exp_id} ({exp_cat})")
            print(f"       Got:      {got_id} ({got_cat}), match_type={match_type}")
    print()
    print("="*72)
    print(f"RESULTS: {passed}/{len(TESTS)} passed  |  {failed} failed")
    print("="*72)
    if failures:
        print("\nFAILED QUERIES:")
        for (q, ec, ei, gc, gi, mt) in failures:
            print(f"  QUERY: {q!r}")
            print(f"    Expected: {ei} ({ec})")
            print(f"    Got:      {gi} ({gc}) [{mt}]")
    return failed == 0

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
