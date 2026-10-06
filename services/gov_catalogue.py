"""
GuideFlow AI - Official Indian Government Service Catalogue
Sourced exclusively from official Indian Government portals and the National Portal of India (india.gov.in).
Strictly adheres to official categories, verified .gov.in/.nic.in domains, and Central/State designations.
"""

from typing import Dict, Any, List, Optional

# Official 18 Service Categories from the National Portal of India (india.gov.in)
OFFICIAL_GOV_CATEGORIES = [
    "Agriculture, Rural & Environment",
    "Benefits & Social Development",
    "Business & Self-employed",
    "Citizenship, Visa & Passports",
    "Defence & Foreign Affairs",
    "Driving & Transport",
    "Education & Learning",
    "Governance & Planning",
    "Health & Wellness",
    "Housing & Local Services",
    "Infrastructure & Industries",
    "Jobs",
    "Justice, Law & Grievances",
    "Money & Taxes",
    "Science, IT & Communication",
    "Travel & Tourism",
    "Welfare of Families",
    "Youth, Sports & Culture"
]

# Structured Master Catalogue of Official Indian Government Services
GOVERNMENT_SERVICES_CATALOGUE: List[Dict[str, Any]] = [
    # 1. Education & Learning -> Scholarships
    {
        "service_id": "nsp_scholarship",
        "service_name": {
            "en": "National Scholarship Portal (NSP)",
            "te": "జాతీయ స్కాలర్‌షిప్ పోర్టల్ (NSP)",
            "hi": "राष्ट्रीय छात्रवृत्ति पोर्टल (NSP)"
        },
        "category": "Education & Learning",
        "government_level": "Central",
        "department": "Ministry of Electronics & IT / Ministry of Education, Government of India",
        "official_url": "https://scholarships.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/education",
        "keywords": [
            "scholarship", "scholarships", "student scholarship", "college scholarship",
            "education scholarship", "fellowship", "stipend", "financial help for college",
            "financial aid for study", "pre-matric", "post-matric", "vidyarthi",
            "స్కాలర్‌షిప్", "విద్యార్థి వేతనం", "విద్యా స్కాలర్‌షిప్", "కాలేజీ సహాయం",
            "छात्रवृत्ति", "स्कॉलरशिप", "विद्यार्थी छात्रवृत्ति", "कॉलेज छात्रवृत्ति", "वजीफा"
        ],
        "aliases": [
            "NSP", "National Scholarship", "Student Scholarship", "Post Matric Scholarship",
            "Pre Matric Scholarship", "Central Sector Scholarship Scheme", "NSP Portal",
            "Higher Education Scholarship", "Financial Help for College", "Scholarship Scheme"
        ],
        "negative_keywords": [
            "hospital", "doctor", "appointment", "clinic", "ors", "driving", "licence",
            "ration", "passport", "police", "vehicle"
        ],
        "description": {
            "en": "Official Government of India portal for pre-matric, post-matric, and higher education scholarships for students across India.",
            "te": "భారతదేశం అంతటా విద్యార్థుల కోసం ప్రీ-మెట్రిక్, పోస్ట్-మెట్రిక్ మరియు ఉన్నత విద్యా స్కాలర్‌షిప్‌ల కోసం అధికారిక కేంద్ర ప్రభుత్వ పోర్టల్.",
            "hi": "भारत भर के छात्रों के लिए प्री-मैट्रिक, पोस्ट-मैट्रिक और उच्च शिक्षा छात्रवृत्ति के लिए आधिकारिक सरकारी पोर्टल।"
        },
        "required_items": ["Aadhaar Number", "Student Bank Account Passbook", "Previous Marksheet", "Income Certificate"],
        "typical_steps": [
            {
                "title": "Open the official National Scholarship Portal",
                "action": "Visit the official portal at scholarships.gov.in. Verify the web address has '.gov.in' at the end.",
                "tip": "Look for the button labeled 'Student Registration' or 'Apply for Scholarship'.",
                "simplified": "Open the official scholarship website. Look for the registration button."
            },
            {
                "title": "Register with your Aadhaar and Mobile Number",
                "action": "Provide your Aadhaar number and enter the confirmation OTP code sent to your linked phone.",
                "tip": "Keep your Aadhaar-linked mobile phone near you to read the code.",
                "simplified": "Type your Aadhaar number and the code that comes on your phone."
            },
            {
                "title": "Select your Scheme (Pre-Matric, Post-Matric, or Higher Education)",
                "action": "Choose the scholarship scheme matching your current school, college, or university course.",
                "tip": "If you are in college or degree study, select 'Post-Matric / Higher Education'.",
                "simplified": "Pick the scholarship option for your college or school class."
            },
            {
                "title": "Fill in institution and bank account details",
                "action": "Enter your college name and bank account details where scholarship money will be credited via DBT.",
                "tip": "Ensure the bank account is active and in the student's own name.",
                "simplified": "Type your college name and your bank account number."
            },
            {
                "title": "Submit application and print acknowledgement",
                "action": "Review your application summary, click Submit, and save your application ID for verification.",
                "tip": "Submit a printed copy to your college nodal officer for institutional verification.",
                "simplified": "Check your details and click submit. Save your application number slip."
            }
        ]
    },

    # 2. Citizenship, Visa & Passports -> Passport Seva
    {
        "service_id": "passport_seva",
        "service_name": {
            "en": "Passport Seva Official Portal",
            "te": "పాస్‌పోర్ట్ సేవా అధికారిక పోర్టల్",
            "hi": "पासपोर्ट सेवा आधिकारिक पोर्टल"
        },
        "category": "Citizenship, Visa & Passports",
        "government_level": "Central",
        "department": "Consular, Passport & Visa (CPV) Division, Ministry of External Affairs",
        "official_url": "https://www.passportindia.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/citizenship-visa-passports",
        "keywords": [
            "passport", "passports", "passport seva", "new passport", "apply passport",
            "apply for passport", "passport renewal", "tatkaal passport", "reissue passport",
            "passport kendra", "psk appointment", "mea passport",
            "పాస్‌పోర్ట్", "కొత్త పాస్‌పోర్ట్", "పాస్‌పోర్ట్ సేవా", "పాస్‌పోర్టు దరఖాస్తు",
            "पासपोर्ट", "नया पासपोर्ट", "पासपोर्ट सेवा", "पासपोर्ट आवेदन", "तत्काल पासपोर्ट"
        ],
        "aliases": [
            "Passport Seva", "Apply for Passport", "New Passport Application",
            "Passport Renewal", "Tatkaal Passport", "Passport Kendra Appointment"
        ],
        "negative_keywords": [
            "hospital", "doctor", "appointment doctor", "scholarship", "driving", "ration", "electricity"
        ],
        "description": {
            "en": "Official Ministry of External Affairs portal to apply for fresh Indian passports, renewals, and book appointments at Passport Seva Kendras.",
            "te": "కొత్త భారతీయ పాస్‌పోర్ట్, పునరుద్ధరణ మరియు పాస్‌పోర్ట్ సేవా కేంద్రాలలో అపాయింట్‌మెంట్‌ల కోసం అధికారిక విదేశీ వ్యవహారాల మంత్రిత్వ శాఖ పోర్టల్.",
            "hi": "नए भारतीय पासपोर्ट, नवीनीकरण और पासपोर्ट सेवा केंद्रों पर अपॉइंटमेंट बुक करने के लिए आधिकारिक विदेश मंत्रालय का पोर्टल।"
        },
        "required_items": ["Aadhaar Card", "Proof of Date of Birth (Birth Certificate or 10th Certificate)", "Address Proof"],
        "typical_steps": [
            {
                "title": "Open Passport Seva official portal",
                "action": "Visit passportindia.gov.in. Ensure the site URL ends with '.gov.in'.",
                "tip": "Click on 'New User Registration' on the home page.",
                "simplified": "Open the official passport website by clicking the link."
            },
            {
                "title": "Register an account and log in",
                "action": "Create your login account with your email address and select your nearest Passport Office.",
                "tip": "Remember your login ID and password for future appointment tracking.",
                "simplified": "Create your account using your email and sign in."
            },
            {
                "title": "Fill the Online Application for Fresh / Reissue Passport",
                "action": "Select 'Apply for Fresh Passport' and enter your personal, family, and address details carefully.",
                "tip": "Enter your name exactly as written on your Aadhaar card and school records.",
                "simplified": "Type your name, address, and parents' names as printed on your Aadhaar card."
            },
            {
                "title": "Pay fee and schedule Passport Seva Kendra (PSK) appointment",
                "action": "Make the online fee payment and choose a convenient date and time slot at your nearest PSK or Post Office PSK.",
                "tip": "Save the appointment confirmation SMS and print the application receipt.",
                "simplified": "Pay the government fee and choose a convenient day to visit the passport office."
            },
            {
                "title": "Visit Passport Seva Kendra with original documents",
                "action": "Carry your original Aadhaar card, date of birth proof, and address proof for biometric verification.",
                "tip": "Arrive 15 minutes before your scheduled appointment time.",
                "simplified": "Visit the passport office on your appointment day with your original documents."
            }
        ]
    },

    # 3. Citizenship, Visa & Passports -> Aadhaar (myAadhaar)
    {
        "service_id": "myaadhaar_services",
        "service_name": {
            "en": "myAadhaar Citizen Portal (UIDAI)",
            "te": "మై ఆధార్ అధికారిక పోర్టల్ (UIDAI)",
            "hi": "माई आधार आधिकारिक पोर्टल (UIDAI)"
        },
        "category": "Citizenship, Visa & Passports",
        "government_level": "Central",
        "department": "Unique Identification Authority of India (UIDAI)",
        "official_url": "https://myaadhaar.uidai.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/citizenship-visa-passports",
        "keywords": [
            "aadhaar", "aadhar", "uidai", "myaadhaar", "download aadhaar", "update aadhaar",
            "aadhaar card", "pvc aadhaar", "aadhaar address update", "check aadhaar status",
            "aadhaar pvc card", "aadhaar link", "eaadhaar",
            "ఆధార్", "ఆధార్ కార్డు", "ఆధార్ డౌన్‌లోడ్", "ఆధార్ అప్‌డేట్", "పీవీసీ ఆధార్",
            "आधार", "आधार कार्ड", "आधार डाउनलोड", "आधार अपडेट", "पीवीसी आधार कार्ड"
        ],
        "aliases": [
            "myAadhaar", "UIDAI Portal", "Download Aadhaar", "Aadhaar Card",
            "Aadhaar Update", "Order Aadhaar PVC Card", "e-Aadhaar"
        ],
        "negative_keywords": [
            "scholarship", "hospital", "doctor", "driving", "ration", "passport"
        ],
        "description": {
            "en": "Official UIDAI citizen portal to download digital Aadhaar, update residential address, order PVC card, and verify biometric status.",
            "te": "డిజిటల్ ఆధార్ డౌన్‌లోడ్ చేయడానికి, చిరునామాను అప్‌డేట్ చేయడానికి మరియు PVC కార్డును ఆర్డర్ చేయడానికి అధికారిక UIDAI పోర్టల్.",
            "hi": "डिजिटल आधार डाउनलोड करने, पता अपडेट करने, पीवीसी कार्ड ऑर्डर करने के लिए आधिकारिक यूआईडीएआई पोर्टल।"
        },
        "required_items": ["12-digit Aadhaar Number", "Mobile number linked with Aadhaar"],
        "typical_steps": [
            {
                "title": "Open the myAadhaar official portal",
                "action": "Go to myaadhaar.uidai.gov.in. Verify that the web address has '.gov.in' at the end.",
                "tip": "Look for the large blue 'Login' button on the right side.",
                "simplified": "Click the link to go to the official Aadhaar website. Look for the blue 'Login' button."
            },
            {
                "title": "Login with Aadhaar and OTP",
                "action": "Enter your 12-digit Aadhaar number and the security letters (Captcha). Click 'Send OTP'.",
                "tip": "The OTP will arrive on the phone number linked with your Aadhaar.",
                "simplified": "Type your 12-digit Aadhaar number. A code will come to your mobile. Enter it to sign in."
            },
            {
                "title": "Select your required service",
                "action": "Choose from 'Download Aadhaar', 'Order Aadhaar PVC Card', or 'Address Update'.",
                "tip": "Downloading an electronic Aadhaar PDF is completely free.",
                "simplified": "Click what you want: download your card, order a plastic card, or update your address."
            },
            {
                "title": "Follow the on-screen confirmation",
                "action": "Review the details shown on the screen and click Submit.",
                "tip": "Your electronic card password is the first 4 letters of your name in CAPITAL letters plus your birth year (e.g. SURE1955).",
                "simplified": "Confirm your details. The password to open the file is your name in capital letters plus your birth year."
            }
        ]
    },

    # 4. Money & Taxes -> PAN Card Services
    {
        "service_id": "pan_card_service",
        "service_name": {
            "en": "PAN Card Official Services (Instant e-PAN & NSDL)",
            "te": "పాన్ కార్డు అధికారిక సేవలు (ఇన్‌స్టంట్ ఈ-పాన్ & NSDL)",
            "hi": "पैन कार्ड आधिकारिक सेवाएं (तत्काल ई-पैन एवं एनएसडीएल)"
        },
        "category": "Money & Taxes",
        "government_level": "Central",
        "department": "Income Tax Department, Ministry of Finance, Government of India",
        "official_url": "https://www.incometax.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/money-taxes",
        "keywords": [
            "pan", "pan card", "apply pan", "apply pan card", "instant pan", "instant e-pan",
            "pan aadhaar link", "permanent account number", "nsdl pan", "uti pan", "pan correction",
            "ప్యాన్", "పాన్ కార్డు", "కొత్త పాన్ కార్డు", "పాన్ ఆధార్ లింక్",
            "पैन", "पैन कार्ड", "पैन कार्ड आवेदन", "तत्काल ई-पैन", "पैन आधार लिंक"
        ],
        "aliases": [
            "PAN Card", "Instant e-PAN", "Apply for PAN Card", "Income Tax PAN",
            "PAN-Aadhaar Linking", "Protean NSDL PAN", "UTIITSL PAN"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "ration", "passport"
        ],
        "description": {
            "en": "Official Income Tax Department service to generate instant digital e-PAN free of cost using Aadhaar, or apply for physical PAN cards.",
            "te": "ఆధార్ ఉపయోగించి ఉచితంగా ఇన్‌స్టంట్ డిజిటల్ ఈ-పాన్ పొందడానికి లేదా కొత్త పాన్ కార్డు కోసం అధికారిక ఆదాయపు పన్ను శాఖ సేవ.",
            "hi": "आधार का उपयोग करके तुरंत नि:शुल्क डिजिटल ई-पैन प्राप्त करने या नए पैन कार्ड के लिए आधिकारिक आयकर विभाग सेवा।"
        },
        "required_items": ["Aadhaar Number", "Mobile linked with Aadhaar"],
        "typical_steps": [
            {
                "title": "Open the official Income Tax e-Filing portal",
                "action": "Visit incometax.gov.in and click on 'Instant e-PAN' under Quick Links.",
                "tip": "Instant e-PAN is completely paperless and free for Aadhaar holders.",
                "simplified": "Open the official Income Tax portal and click on 'Instant e-PAN'."
            },
            {
                "title": "Click on 'Get New e-PAN'",
                "action": "Select 'Get New e-PAN' and enter your 12-digit Aadhaar number.",
                "tip": "Make sure your mobile number is linked to your Aadhaar to receive verification OTP.",
                "simplified": "Type your 12-digit Aadhaar number and click continue."
            },
            {
                "title": "Verify with Aadhaar OTP",
                "action": "Enter the 6-digit OTP code received on your mobile phone to validate your Aadhaar details.",
                "tip": "Review your photo, name, and date of birth fetched from Aadhaar.",
                "simplified": "Type the 6-digit code received on your phone to confirm your identity."
            },
            {
                "title": "Download your official e-PAN",
                "action": "Your PAN will be allotted within 10 minutes. Return to the same page to download your digital PAN card.",
                "tip": "The downloaded PDF is fully valid for all financial and banking purposes.",
                "simplified": "Wait a few minutes and download your digital PAN card."
            }
        ]
    },

    # 5. Citizenship, Visa & Passports -> Voter ID (ECI)
    {
        "service_id": "voter_services",
        "service_name": {
            "en": "Voters' Services Official Portal (ECI)",
            "te": "ఓటరు సేవల అధికారిక పోర్టల్ (ECI)",
            "hi": "मतदाता सेवा आधिकारिक पोर्टल (ECI)"
        },
        "category": "Citizenship, Visa & Passports",
        "government_level": "Central",
        "department": "Election Commission of India (ECI)",
        "official_url": "https://voters.eci.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/governance-planning",
        "keywords": [
            "voter", "voter id", "voter card", "epic", "nvsp", "new voter registration",
            "download epic", "election card", "voter list", "electoral roll", "shift voter id",
            "ఓటరు", "ఓటర్ కార్డు", "ఎలక్షన్ కార్డు", "ఓటరు నమోదు", "ఎపిక్ కార్డు",
            "मतदाता", "वोटर आईडी", "पहचान पत्र", "मतदाता पहचान पत्र", "वोटर कार्ड", "चुनाव कार्ड"
        ],
        "aliases": [
            "Voter ID", "Voters Service Portal", "NVSP Portal", "EPIC Download",
            "New Voter Registration", "Form 6 Voter ID", "Election Commission Portal"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "ration", "electricity"
        ],
        "description": {
            "en": "Official Election Commission of India portal for new voter registration (Form 6), downloading digital e-EPIC cards, and checking electoral roll status.",
            "te": "కొత్త ఓటరు నమోదు (ఫారం 6), డిజిటల్ ఈ-ఎపిక్ కార్డు డౌన్‌లోడ్ మరియు ఓటరు జాబితా స్థితి తనిఖీ కోసం భారత ఎన్నికల సంఘం అధికారిక పోర్టల్.",
            "hi": "नए मतदाता पंजीकरण (फॉर्म 6), डिजिटल ई-एपिक कार्ड डाउनलोड और मतदाता सूची स्थिति जांचने के लिए भारत निर्वाचन आयोग का आधिकारिक पोर्टल।"
        },
        "required_items": ["Passport Size Photograph", "Age Proof (Aadhaar/Birth Certificate)", "Address Proof"],
        "typical_steps": [
            {
                "title": "Open the official Voters' Services Portal",
                "action": "Visit voters.eci.gov.in. Verify the web address ends with '.gov.in'.",
                "tip": "Look for 'Sign-Up' or 'Login' at the top right.",
                "simplified": "Open the election commission website by clicking the link."
            },
            {
                "title": "Select your required Voter service",
                "action": "Click 'Fill Form 6' for new voter registration, or 'E-EPIC Download' to get your existing voter card.",
                "tip": "If you already have a voter ID number (EPIC), you can download the digital card directly.",
                "simplified": "Choose 'Form 6' for a new card or 'Download' if you already have one."
            },
            {
                "title": "Fill your assembly constituency and personal details",
                "action": "Select your state, district, and constituency, and enter your full name and date of birth.",
                "tip": "Upload clear photos of your address proof and identity proof.",
                "simplified": "Type your name, address, and your assembly area."
            },
            {
                "title": "Submit and note reference number",
                "action": "Submit the form and save the generated tracking reference number for verification by the Booth Level Officer (BLO).",
                "tip": "Your physical voter card will be delivered by Speed Post to your home address free of charge.",
                "simplified": "Save your reference number. Your card will arrive by post at your home."
            }
        ]
    },

    # 6. Driving & Transport -> Parivahan Sarathi (Driving Licence)
    {
        "service_id": "driving_licence_sarathi",
        "service_name": {
            "en": "Parivahan Sarathi (Driving Licence Services)",
            "te": "పరివాహన్ సారథి (డ్రైవింగ్ లైసెన్స్ సేవలు)",
            "hi": "परिवहन सारथी (ड्राइविंग लाइसेंस सेवाएं)"
        },
        "category": "Driving & Transport",
        "government_level": "Central",
        "department": "Ministry of Road Transport and Highways (MoRTH), Government of India",
        "official_url": "https://parivahan.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/driving-transport",
        "keywords": [
            "driving licence", "driving license", "learner licence", "learner license",
            "llr", "dl", "renew driving license", "parivahan", "sarathi", "driving test",
            "rto services", "permanent dl", "vehicle licence",
            "డ్రైవింగ్ లైసెన్స్", "సారథి", "లైసెన్స్", "లెర్నర్ లైసెన్స్", "ఎల్ఎల్ఆర్",
            "ड्राइविंग लाइसेंस", "लर्नर लाइसेंस", "सारथी", "डीएल", "ड्राइविंग टेस्ट", "परिवहन"
        ],
        "aliases": [
            "Driving Licence", "Learner Licence", "Sarathi Parivahan", "DL Renewal",
            "LLR Application", "Driving License Portal", "RTO Driving Licence"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "ration", "pension", "caste"
        ],
        "description": {
            "en": "Official Ministry of Road Transport and Highways portal for Learner's Licence (LLR), Driving Licence (DL) applications, renewals, and duplicate licences.",
            "te": "లెర్నర్స్ లైసెన్స్ (LLR), డ్రైవింగ్ లైసెన్స్ (DL) దరఖాస్తులు మరియు పునరుద్ధరణల కోసం రహదారి రవాణా మంత్రిత్వ శాఖ అధికారిక పోర్టల్.",
            "hi": "लर्नर लाइसेंस (एलएलआर), ड्राइविंग लाइसेंस (डीएल) आवेदन और नवीनीकरण के लिए सड़क परिवहन मंत्रालय का आधिकारिक पोर्टल।"
        },
        "required_items": ["Aadhaar Card", "Age Proof (School Certificate or Birth Certificate)", "Passport Photo"],
        "typical_steps": [
            {
                "title": "Open Parivahan Sarathi portal",
                "action": "Visit parivahan.gov.in and click on 'Driving School / Licence Related Services'.",
                "tip": "Select your state from the dropdown list to open your state transport portal.",
                "simplified": "Open the official Parivahan website and choose your home state."
            },
            {
                "title": "Choose 'Apply for Learner Licence' or 'Driving Licence'",
                "action": "If you are applying for the first time, click 'Apply for Learner Licence (LL)'.",
                "tip": "With Aadhaar authentication, you can take the online learner test from home in most states.",
                "simplified": "Click 'Apply for Learner Licence' to start your application."
            },
            {
                "title": "Authenticate with Aadhaar and fill application",
                "action": "Authenticate with your Aadhaar OTP so personal details and address are pre-filled automatically.",
                "tip": "Select the vehicle category (e.g. Motorcycle with Gear, Light Motor Vehicle - Car).",
                "simplified": "Use your Aadhaar to fill in your personal details automatically."
            },
            {
                "title": "Pay fee and complete the online traffic test",
                "action": "Pay the government testing fee online and complete the basic road safety audio-visual test.",
                "tip": "Once passed, download your digital Learner Licence immediately.",
                "simplified": "Pay the test fee and answer simple road safety questions online to get your learner licence."
            }
        ]
    },

    # 7. Benefits & Social Development -> Ration Card / NFSA
    {
        "service_id": "ration_card_nfsa",
        "service_name": {
            "en": "National Food Security Portal (Ration Card Services)",
            "te": "జాతీయ ఆహార భద్రతా పోర్టల్ (రేషన్ కార్డు సేవలు)",
            "hi": "राष्ट्रीय खाद्य सुरक्षा पोर्टल (राशन कार्ड सेवाएं)"
        },
        "category": "Benefits & Social Development",
        "government_level": "Central",
        "department": "Department of Food and Public Distribution, Government of India",
        "official_url": "https://nfsa.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/benefits-social-development",
        "keywords": [
            "ration card", "ration", "food card", "new ration card", "nfsa", "pds",
            "annavitran", "apply ration card", "ration card status", "food security card",
            "bpl ration card", "onorc", "ration shop",
            "రేషన్ కార్డు", "ఆహార కార్డు", "రేషన్", "రాషన్ కార్డు", "ఆహార భద్రత",
            "राशन कार्ड", "खाद्य कार्ड", "राशन", "नया राशन कार्ड", "एनएफएसए", "राशन पर्ची"
        ],
        "aliases": [
            "Ration Card", "NFSA Portal", "Food Security Card", "New Ration Card",
            "One Nation One Ration Card", "Ration Card Application", "PDS Ration"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "passport"
        ],
        "description": {
            "en": "Official National Food Security Portal to apply for new ration cards, check PDS allocation, find fair price shops, and manage One Nation One Ration Card.",
            "te": "కొత్త రేషన్ కార్డుల కోసం దరఖాస్తు చేసుకోవడానికి, ప్రజా పంపిణీ కోటాను తనిఖీ చేయడానికి మరియు రేషన్ దుకాణాలను కనుగొనడానికి అధికారిక జాతీయ పోర్టల్.",
            "hi": "नए राशन कार्ड के लिए आवेदन करने, राशन कोटा जांचने और उचित मूल्य की दुकानें खोजने के लिए आधिकारिक राष्ट्रीय पोर्टल।"
        },
        "required_items": ["Aadhaar Cards of All Family Members", "Income Certificate", "Electricity/Gas Bill for Address Proof"],
        "typical_steps": [
            {
                "title": "Open the official National Food Security Portal",
                "action": "Visit nfsa.gov.in. Verify that the address ends with '.gov.in'.",
                "tip": "Click on 'Citizen Corner' or 'Apply for New Ration Card'.",
                "simplified": "Open the official government food security website by clicking the link."
            },
            {
                "title": "Select your State Food Department",
                "action": "Choose your state from the state portal directory to access your state Civil Supplies system.",
                "tip": "Ration cards are administered by State Civil Supplies Departments.",
                "simplified": "Select your state from the list."
            },
            {
                "title": "Add family member details and Aadhaar numbers",
                "action": "Enter the head of family details and add all family members with their 12-digit Aadhaar numbers.",
                "tip": "Ensure all names match their respective Aadhaar cards.",
                "simplified": "Type the names and Aadhaar numbers of all members living in your household."
            },
            {
                "title": "Submit application and note acknowledgement number",
                "action": "Upload required address and income proof documents and submit for local revenue verification.",
                "tip": "You can track ration card approval online using your acknowledgement number.",
                "simplified": "Save your receipt number. The local food office will verify and issue your card."
            }
        ]
    },

    # 8. Housing & Local Services -> Birth Certificate (CRS)
    {
        "service_id": "birth_certificate_crs",
        "service_name": {
            "en": "Civil Registration System (Birth Certificate)",
            "te": "సివిల్ రిజిస్ట్రేషన్ సిస్టమ్ (జనన ధృవీకరణ పత్రం)",
            "hi": "नागरिक पंजीकरण प्रणाली (जन्म प्रमाण पत्र)"
        },
        "category": "Housing & Local Services",
        "government_level": "Central",
        "department": "Office of the Registrar General of India, Ministry of Home Affairs",
        "official_url": "https://crsorgi.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/housing-local-services",
        "keywords": [
            "birth certificate", "birth registration", "apply birth certificate",
            "download birth certificate", "crs", "municipal birth record", "birth certificate online",
            "జనన ధృవీకరణ", "జనన సర్టిఫికేట్", "బర్త్ సర్టిఫికేట్", "జనన నమోదు",
            "जन्म प्रमाण पत्र", "जन्म पंजीकरण", "बर्थ सर्टिफिकेट", "जन्म प्रमाण पत्र ऑनलाइन"
        ],
        "aliases": [
            "Birth Certificate", "Civil Registration System", "CRS Org",
            "Birth Registration", "Municipal Birth Certificate", "Download Birth Certificate"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "ration", "electricity"
        ],
        "description": {
            "en": "Official Civil Registration System portal by the Registrar General of India for reporting births, tracking registration, and generating verified birth certificates.",
            "te": "జననాలను నమోదు చేయడానికి మరియు ధృవీకరించబడిన జనన ధృవీకరణ పత్రాలను పొందడానికి భారత రిజిస్ట్రార్ జనరల్ అధికారిక పోర్టల్.",
            "hi": "जन्म की रिपोर्ट करने और सत्यापित जन्म प्रमाण पत्र प्राप्त करने के लिए भारत के महारजिस्ट्रार का आधिकारिक पोर्टल।"
        },
        "required_items": ["Hospital Discharge Slip / Proof of Birth", "Parents' Aadhaar Cards", "Marriage Certificate or Identification"],
        "typical_steps": [
            {
                "title": "Open the official Civil Registration System portal",
                "action": "Visit crsorgi.gov.in. Verify that the domain ends with '.gov.in'.",
                "tip": "Click on 'General Public Signup' to access birth services.",
                "simplified": "Open the official civil registration website by clicking the link."
            },
            {
                "title": "Fill the Birth Registration Form",
                "action": "Enter child name, gender, date of birth, place of birth (hospital or home), and parents' details.",
                "tip": "Ensure the hospital discharge slip or institutional record number is entered accurately.",
                "simplified": "Type the baby's name, birth date, hospital name, and parents' details."
            },
            {
                "title": "Submit to local registrar / municipal office",
                "action": "Submit the completed application form to the jurisdictional Registrar of Births and Deaths.",
                "tip": "Births reported within 21 days are registered without any delayed registration penalty.",
                "simplified": "Submit the form online to your municipal registrar office."
            },
            {
                "title": "Download digitally signed Birth Certificate",
                "action": "Once approved, download the digitally signed QR-coded birth certificate from the portal.",
                "tip": "The digital certificate with QR code is legally valid nationwide without physical stamps.",
                "simplified": "Download your official digital birth certificate with QR code."
            }
        ]
    },

    # 9. Benefits & Social Development -> Caste Certificate
    {
        "service_id": "caste_certificate_service",
        "service_name": {
            "en": "State Citizen Services (Caste Certificate)",
            "te": "రాష్ట్ర పౌర సేవలు (కుల ధృవీకరణ పత్రం)",
            "hi": "राज्य नागरिक सेवाएं (जाति प्रमाण पत्र)"
        },
        "category": "Benefits & Social Development",
        "government_level": "State",
        "department": "Revenue & Backward Classes Welfare Departments, State Governments (via National Portal)",
        "official_url": "https://www.india.gov.in/topics/benefits-social-development",
        "india_gov_reference": "https://www.india.gov.in/topics/benefits-social-development",
        "keywords": [
            "caste certificate", "community certificate", "sc st obc certificate",
            "apply caste certificate", "revenue caste certificate", "caste verification",
            "కుల ధృవీకరణ", "కుల సర్టిఫికేట్", "క్యాస్ట్ సర్టిఫికేట్", "కమ్యూనిటీ సర్టిఫికేట్",
            "जाति प्रमाण पत्र", "एससी एसटी प्रमाण पत्र", "ओबीसी प्रमाण पत्र", "जाति प्रमाणपत्र"
        ],
        "aliases": [
            "Caste Certificate", "Community Certificate", "SC ST OBC Certificate",
            "State Revenue Caste Certificate", "Apply Caste Certificate"
        ],
        "negative_keywords": [
            "hospital", "doctor", "driving", "passport", "electricity"
        ],
        "description": {
            "en": "Official State Government revenue services accessible via the National Portal of India to apply for verified SC, ST, OBC, or Community certificates.",
            "te": "ధృవీకరించబడిన SC, ST, OBC లేదా కమ్యూనిటీ సర్టిఫికేట్ల కోసం దరఖాస్తు చేసుకోవడానికి జాతీయ పోర్టల్ ద్వారా అందుబాటులో ఉన్న రాష్ట్ర ప్రభుత్వ అధికారిక రెవెన్యూ సేవ.",
            "hi": "सत्यापित एससी, एसटी, ओबीसी या समुदाय प्रमाण पत्र के लिए राष्ट्रीय पोर्टल के माध्यम से उपलब्ध आधिकारिक राज्य सरकारी राजस्व सेवा।"
        },
        "required_items": ["Aadhaar Card", "Father's/Family Caste Proof", "Ration Card or Residential Proof"],
        "typical_steps": [
            {
                "title": "Access your State Citizen Service portal",
                "action": "Visit the official State Revenue service (e.g. MeeSeva, e-District, RTPS) through india.gov.in.",
                "tip": "Verify the state portal web address ends with '.gov.in'.",
                "simplified": "Open your official state citizen portal from the link provided."
            },
            {
                "title": "Select 'Revenue Services' -> 'Caste Certificate'",
                "action": "Choose the application for SC, ST, BC, or OBC Community Certificate.",
                "tip": "Keep family records or parents' school transfer certificates handy for sub-caste verification.",
                "simplified": "Click on 'Caste Certificate' under revenue services."
            },
            {
                "title": "Enter applicant details and upload documentation",
                "action": "Type applicant name, father's name, address, and upload identity and caste lineage documents.",
                "tip": "Ensure the applicant's name matches their school records.",
                "simplified": "Enter your name, father's name, and upload your Aadhaar and family documents."
            },
            {
                "title": "Tahsildar verification and digital certificate download",
                "action": "The application is verified by the Revenue Inspector/Tahsildar and issued with a digital signature.",
                "tip": "Download the digitally signed certificate online using your application token.",
                "simplified": "After revenue verification, download your official digitally signed certificate."
            }
        ]
    },

    # 10. Benefits & Social Development -> Income Certificate
    {
        "service_id": "income_certificate_service",
        "service_name": {
            "en": "State Citizen Services (Income Certificate)",
            "te": "రాష్ట్ర పౌర సేవలు (ఆదాయ ధృవీకరణ పత్రం)",
            "hi": "राज्य नागरिक सेवाएं (आय प्रमाण पत्र)"
        },
        "category": "Benefits & Social Development",
        "government_level": "State",
        "department": "Revenue Departments, State Governments (via National Portal of India)",
        "official_url": "https://www.india.gov.in/topics/benefits-social-development",
        "india_gov_reference": "https://www.india.gov.in/topics/benefits-social-development",
        "keywords": [
            "income certificate", "annual income certificate", "apply income certificate",
            "tahsildar income certificate", "family income proof", "income certificate online",
            "ఆదాయ ధృవీకరణ", "ఆదాయ సర్టిఫికేట్", "ఇన్‌కమ్ సర్టిఫికేట్", "ఆదాయ ధృవపత్రం",
            "आय प्रमाण पत्र", "वार्षिक आय प्रमाण पत्र", "आय प्रमाणपत्र", "तहसील आय प्रमाण पत्र"
        ],
        "aliases": [
            "Income Certificate", "Annual Income Certificate", "Tahsil Income Certificate",
            "Revenue Income Certificate", "Family Income Certificate"
        ],
        "negative_keywords": [
            "hospital", "doctor", "driving", "passport", "electricity"
        ],
        "description": {
            "en": "Official State Government revenue portal to obtain certified annual income certificates for educational fee reimbursement, scholarships, and welfare schemes.",
            "te": "ఫీజు రీయింబర్స్‌మెంట్, స్కాలర్‌షిప్‌లు మరియు ప్రభుత్వ సంక్షేమ పథకాల కోసం వార్షిక ఆదాయ ధృవీకరణ పత్రం పొందేందుకు అధికారిక రాష్ట్ర రెవెన్యూ సేవ.",
            "hi": "फीस प्रतिपूर्ति, छात्रवृत्ति और सरकारी कल्याणकारी योजनाओं के लिए प्रमाणित वार्षिक आय प्रमाण पत्र प्राप्त करने हेतु आधिकारिक राज्य राजस्व सेवा।"
        },
        "required_items": ["Aadhaar Card", "Salary Slip / Income Declaration Form", "Ration Card or Residential Proof"],
        "typical_steps": [
            {
                "title": "Open your State Revenue / e-District portal",
                "action": "Visit your official state service portal (e.g. MeeSeva, e-District) through india.gov.in.",
                "tip": "Ensure the portal has '.gov.in' at the end of the address.",
                "simplified": "Open your state online citizen service portal."
            },
            {
                "title": "Select 'Issue of Income Certificate'",
                "action": "Choose the Income Certificate application option under the Revenue Department category.",
                "tip": "Select the purpose of certificate (e.g. Education, Scholarship, or General).",
                "simplified": "Click on 'Income Certificate' option."
            },
            {
                "title": "Enter annual household income details",
                "action": "Declare total annual earnings from salary, agriculture, business, or other sources.",
                "tip": "Attach salary slips, pension statements, or land revenue receipts as supporting proof.",
                "simplified": "Type your family's yearly income and upload supporting documents."
            },
            {
                "title": "Download the verified Income Certificate",
                "action": "Once approved by the Revenue Inspector/Tahsildar, download your digitally signed certificate.",
                "tip": "Income certificates are typically valid for one financial year.",
                "simplified": "Download your official Income Certificate after local revenue approval."
            }
        ]
    },

    # 11. Welfare of Families -> Pension / Jeevan Pramaan
    {
        "service_id": "pension_services",
        "service_name": {
            "en": "Jeevan Pramaan & National Social Assistance (Pension)",
            "te": "జీవన్ ప్రమాణ్ & జాతీయ పెన్షన్ సేవలు",
            "hi": "जीवन प्रमाण एवं राष्ट्रीय पेंशन सेवाएं"
        },
        "category": "Welfare of Families",
        "government_level": "Central",
        "department": "Ministry of Electronics & IT / Ministry of Rural Development, Government of India",
        "official_url": "https://jeevanpramaan.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/welfare-families",
        "keywords": [
            "pension", "old age pension", "pension application", "jeevan pramaan",
            "life certificate", "digital life certificate", "senior citizen pension",
            "nsap", "widow pension", "disability pension", "pensioner certificate",
            "పెన్షన్", "వృద్ధాప్య పెన్షన్", "జీవన్ ప్రమాణ్", "లైఫ్ సర్టిఫికేట్", "పెన్షన్ దరఖాస్తు",
            "पेंशन", "वृद्धावस्था पेंशन", "जीवन प्रमाण", "जीवन प्रमाण पत्र", "पेंशन आवेदन", "पेंशनर"
        ],
        "aliases": [
            "Jeevan Pramaan", "Old Age Pension", "National Social Assistance Programme",
            "Digital Life Certificate", "NSAP Pension", "Pension Life Certificate"
        ],
        "negative_keywords": [
            "scholarship", "driving", "passport", "electricity", "job"
        ],
        "description": {
            "en": "Official Government of India portal for pensioners to submit annual Digital Life Certificates (Jeevan Pramaan) and access National Social Assistance pensions.",
            "te": "పెన్షనర్లు వార్షిక డిజిటల్ లైఫ్ సర్టిఫికేట్ (జీవన్ ప్రమాణ్) సమర్పించడానికి మరియు జాతీయ సామాజిక సహాయ పెన్షన్ల కోసం అధికారిక ప్రభుత్వ పోర్టల్.",
            "hi": "पेंशनभोगियों के लिए वार्षिक डिजिटल जीवन प्रमाण पत्र जमा करने और राष्ट्रीय सामाजिक सहायता पेंशन के लिए आधिकारिक सरकारी पोर्टल।"
        },
        "required_items": ["PPO Number", "Pension Bank Account Passbook", "Aadhaar Card"],
        "typical_steps": [
            {
                "title": "Open the official Jeevan Pramaan portal",
                "action": "Visit jeevanpramaan.gov.in. Verify that the web address has '.gov.in' at the end.",
                "tip": "Pensioners can generate certificates from home using the official Face Authentication App.",
                "simplified": "Open the official government pension website."
            },
            {
                "title": "Enter your PPO number and Pension details",
                "action": "Locate your Pension Payment Order (PPO) number on your pension book and enter it.",
                "tip": "Make sure your bank account number matches the account where pension is deposited.",
                "simplified": "Type your PPO number from your pension book and confirm your bank name."
            },
            {
                "title": "Complete Face or Fingerprint Verification",
                "action": "Use the Jeevan Pramaan mobile face recognition app, or visit a postman via India Post Payments Bank at your doorstep.",
                "tip": "A postman can also come to your home to take your fingerprint for Jeevan Pramaan.",
                "simplified": "Look at the phone camera to verify your face, or have a postman help you at your home."
            },
            {
                "title": "Receive confirmation SMS and Pramaan ID",
                "action": "You will receive an SMS containing your Pramaan ID confirming successful submission to your pension disbursing agency.",
                "tip": "Save this SMS for your annual records.",
                "simplified": "Check your phone for a message confirming your certificate is accepted."
            }
        ]
    },

    # 12. Jobs -> National Career Service
    {
        "service_id": "national_career_service",
        "service_name": {
            "en": "National Career Service (Government Jobs Portal)",
            "te": "నేషనల్ కెరీర్ సర్వీస్ (ప్రభుత్వ ఉద్యోగాల పోర్టల్)",
            "hi": "राष्ट्रीय करियर सेवा (सरकारी नौकरी पोर्टल)"
        },
        "category": "Jobs",
        "government_level": "Central",
        "department": "Ministry of Labour and Employment, Government of India",
        "official_url": "https://www.ncs.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/jobs",
        "keywords": [
            "government job", "job registration", "find government jobs", "ncs",
            "employment exchange", "sarkari naukri", "job search", "career portal",
            "government vacancy", "job seeker registration",
            "ప్రభుత్వ ఉద్యోగం", "ఉద్యోగ నమోదు", "ఉద్యోగాలు", "ఉద్యోగ పోర్టల్", "స‌ర్కారీ నౌక‌రీ",
            "सरकारी नौकरी", "रोजगार समाचार", "जॉब रजिस्ट्रेशन", "एनसीएस", "रोजगार मेला", "सरकारी जॉब"
        ],
        "aliases": [
            "National Career Service", "NCS Portal", "Government Job Portal",
            "Sarkari Naukri Portal", "Employment Registration", "Ministry of Labour Jobs"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "ration", "passport"
        ],
        "description": {
            "en": "Official Government of India career portal connecting job seekers with Central, State government vacancies, public sector undertakings, and skill training.",
            "te": "కేంద్ర, రాష్ట్ర ప్రభుత్వ ఉద్యోగ ఖాళీలు మరియు ఉపాధి శిక్షణ కోసం ఉద్యోగార్థులను అనుసంధానించే భారత ప్రభుత్వ అధికారిక పోర్టల్.",
            "hi": "केंद्र व राज्य सरकार की रिक्तियों और कौशल प्रशिक्षण के लिए नौकरी चाहने वालों को जोड़ने वाला भारत सरकार का आधिकारिक पोर्टल।"
        },
        "required_items": ["Aadhaar or National ID", "Educational Qualifications / Degree Certificates", "Updated Resume"],
        "typical_steps": [
            {
                "title": "Open the official National Career Service portal",
                "action": "Visit ncs.gov.in. Verify that the address ends with '.gov.in'.",
                "tip": "Click on 'Jobseeker Registration' on the main page.",
                "simplified": "Open the official government jobs portal by clicking the link."
            },
            {
                "title": "Register with your Aadhaar or Unique Identification",
                "action": "Create your Jobseeker account using your mobile number and verify via OTP.",
                "tip": "Registration on the National Career Service is 100% free of charge.",
                "simplified": "Sign up for free using your mobile number and Aadhaar."
            },
            {
                "title": "Create your digital profile and qualifications",
                "action": "Enter your educational qualifications, work experience, preferred job locations, and language skills.",
                "tip": "Keep your profile up to date to receive SMS alerts for government recruitment drives.",
                "simplified": "Add your educational degree, experience, and the city where you want to work."
            },
            {
                "title": "Search and apply for Government & Public Sector vacancies",
                "action": "Browse verified government and public sector job listings filtered by qualification and apply directly.",
                "tip": "Never pay money to any middleman or agent for government jobs.",
                "simplified": "Search verified government job openings and submit your application."
            }
        ]
    },

    # 13. Money & Taxes -> EPFO / Provident Fund
    {
        "service_id": "epfo_pf_services",
        "service_name": {
            "en": "EPFO Member Unified Portal (Provident Fund)",
            "te": "EPFO ఉద్యోగుల భవిష్య నిధి (PF) పోర్టల్",
            "hi": "ईपीएफओ कर्मचारी भविष्य निधि (पीएफ) पोर्टल"
        },
        "category": "Money & Taxes",
        "government_level": "Central",
        "department": "Employees' Provident Fund Organisation (EPFO), Ministry of Labour and Employment",
        "official_url": "https://www.epfindia.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/money-taxes",
        "keywords": [
            "pf", "epfo", "provident fund", "pf withdrawal", "uan", "epfo member portal",
            "check pf balance", "epf passbook", "pf claim", "pf transfer", "epf online",
            "పీఎఫ్", "భవిష్య నిధి", "పీఎఫ్ బ్యాలెన్స్", "యూఏఎన్", "పీఎఫ్ ఉపసంహరణ",
            "पीएफ", "भविष्य निधि", "पीएफ पासबुक", "ईपीएफओ", "यूएएन", "पीएफ निकासी", "पीएफ बैलेंस"
        ],
        "aliases": [
            "EPFO", "Provident Fund", "UAN Portal", "PF Withdrawal",
            "EPF Passbook", "Member Sewa EPFO", "EPFO Member Portal"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "ration", "passport"
        ],
        "description": {
            "en": "Official EPFO portal for salaried employees to check Provident Fund balance, download EPF passbooks, update KYC, and submit online withdrawal claims.",
            "te": "ఉద్యోగులు తమ భవిష్య నిధి (PF) బ్యాలెన్స్ తనిఖీ చేయడానికి, పాస్‌బుక్ డౌన్‌లోడ్ చేయడానికి మరియు ఉపసంహరణ క్లెయిమ్‌లను సమర్పించడానికి అధికారిక EPFO పోర్టల్.",
            "hi": "कर्मचारियों के लिए भविष्य निधि (पीएफ) बैलेंस जांचने, पासबुक डाउनलोड करने और ऑनलाइन निकासी के लिए आधिकारिक ईपीएफओ पोर्टल।"
        },
        "required_items": ["Universal Account Number (UAN)", "UAN Password", "Aadhaar-linked Mobile Number"],
        "typical_steps": [
            {
                "title": "Open the official EPFO Member Portal",
                "action": "Visit epfindia.gov.in and click on 'Services' -> 'For Employees' -> 'Member UAN/Online Service'.",
                "tip": "Verify the web address ends with '.gov.in'.",
                "simplified": "Open the official EPFO website and go to the Member Portal."
            },
            {
                "title": "Sign in with your 12-digit UAN and Password",
                "action": "Enter your UAN, password, and the security code displayed on the screen.",
                "tip": "If you forgot your password, use the 'Forgot Password' link to reset via mobile OTP.",
                "simplified": "Type your UAN number and password to log in."
            },
            {
                "title": "Check EPF Passbook & Balance",
                "action": "View your total employee and employer contributions and download your official EPF passbook statement.",
                "tip": "Ensure your Aadhaar and bank account are linked under 'Manage' -> 'KYC'.",
                "simplified": "Check how much PF money is saved in your account."
            },
            {
                "title": "Submit Online Claim for PF Withdrawal or Advance",
                "action": "Under 'Online Services', select 'Claim (Form-31, 19, 10C & 10D)' to withdraw funds directly to your verified bank account.",
                "tip": "Online claims are typically processed and credited within 7 to 10 working days.",
                "simplified": "If you need money, choose withdrawal claim and submit directly to your bank."
            }
        ]
    },

    # 14. Housing & Local Services -> Electricity Bill Payment (Bharat BillPay)
    {
        "service_id": "electricity_bill_bbps",
        "service_name": {
            "en": "Bharat BillPay Utility Portal (Electricity Bill)",
            "te": "భారత్ బిల్ పే విద్యుత్ బిల్లు చెల్లింపు",
            "hi": "भारत बिल पे बिजली बिल भुगतान"
        },
        "category": "Housing & Local Services",
        "government_level": "Central",
        "department": "National Payments Corporation of India (NPCI) / State Electricity Boards",
        "official_url": "https://www.bharatbillpay.com/",
        "india_gov_reference": "https://www.india.gov.in/topics/housing-local-services",
        "keywords": [
            "electricity bill", "pay electricity bill", "power bill", "current bill",
            "bijli bill", "discom bill", "consumer number", "bharat billpay", "electric bill",
            "కరెంట్ బిల్లు", "విద్యుత్ బిల్లు", "కరెంటు", "విద్యుత్ బిల్లు చెల్లింపు",
            "बिजली का बिल", "बिजली बिल भुगतान", "बिजली बिल", "विद्युत बिल"
        ],
        "aliases": [
            "Electricity Bill", "Bharat BillPay", "Power Bill Payment",
            "State Electricity DISCOM", "Current Bill Payment", "NPCI BillPay"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "passport", "job", "ration"
        ],
        "description": {
            "en": "Official national interoperable utility payment portal connecting state electricity distribution companies (DISCOMs) across India.",
            "te": "భారతదేశం అంతటా రాష్ట్ర విద్యుత్ పంపిణీ సంస్థలను అనుసంధానించే అధికారిక జాతీయ బిల్లు చెల్లింపు పోర్టల్.",
            "hi": "भारत भर की राज्य बिजली वितरण कंपनियों को जोड़ने वाला आधिकारिक राष्ट्रीय बिल भुगतान पोर्टल।"
        },
        "required_items": ["Consumer / Account Number", "Electricity Bill Paper"],
        "typical_steps": [
            {
                "title": "Open the official electricity payment website",
                "action": "We will open the official portal. Look for the 'Electricity' bill icon.",
                "tip": "Keep your paper electricity bill next to you so you can read your consumer number easily.",
                "simplified": "Tap the blue button to open the bill website. Find the icon with the electric lightning symbol."
            },
            {
                "title": "Select your state and electricity board",
                "action": "Click the dropdown list and select your state (for example, Telangana, Andhra Pradesh, Delhi, or Karnataka).",
                "tip": "The board name is printed in large letters at the top of your paper bill.",
                "simplified": "Choose your state from the list. It is usually the state where your home is located."
            },
            {
                "title": "Enter your Consumer or Service Connection Number",
                "action": "Type the Consumer Number found on your bill paper into the box labeled 'Consumer ID' or 'Account Number'.",
                "tip": "You do not need to enter your name—the system will show it automatically once you enter the number.",
                "simplified": "Look at your paper bill for the 9 to 12 digit consumer number. Type those numbers into the box."
            },
            {
                "title": "Verify your name and the bill amount",
                "action": "The screen will show your name and the amount due. Check if the name matches your bill.",
                "tip": "If the amount or name looks wrong, do not proceed. You can stop anytime.",
                "simplified": "Check if your name appears correctly on screen and see how much money is due."
            },
            {
                "title": "Complete payment safely using UPI or Debit Card",
                "action": "Choose your preferred payment method like UPI (Google Pay / PhonePe) or Net Banking.",
                "tip": "GuideFlow never touches your payment credentials. Never share your bank OTP with anyone.",
                "simplified": "Choose UPI or card. Enter your PIN only on your bank's secure page. We are done!"
            }
        ]
    },

    # 15. Agriculture, Rural & Environment -> Land Records / Bhulekh
    {
        "service_id": "land_records_dilrmp",
        "service_name": {
            "en": "Digital India Land Records & State Bhulekh",
            "te": "డిజిటల్ ఇండియా భూ రికార్డులు & భూలేఖ్",
            "hi": "डिजिटल इंडिया भू-अभिलेख एवं भूलेख"
        },
        "category": "Agriculture, Rural & Environment",
        "government_level": "Central",
        "department": "Department of Land Resources, Ministry of Rural Development, Government of India",
        "official_url": "https://dilrmp.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/agriculture-rural-environment",
        "keywords": [
            "land records", "bhulekh", "patta", "khasra", "khatauni", "ror", "land registry",
            "survey number", "digital land records", "land ownership", "land map", "bhu naksha",
            "భూ రికార్డులు", "పట్టా", "భూలేఖ్", "భూమి సర్వే", "పహానీ", "భూ యాజమాన్యం",
            "भूलेख", "खसरा खतौनी", "जमीन के कागजात", "भू-अभिलेख", "भू नक्शा", "पट्ठा", "जमीन की नकल"
        ],
        "aliases": [
            "Land Records", "Bhulekh Portal", "DILRMP", "Patta Chitta",
            "Khasra Khatauni", "Record of Rights (ROR)", "Digital Land Records"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "passport", "electricity"
        ],
        "description": {
            "en": "Official Digital India Land Records Modernization Programme portal connecting state land records (Bhulekh, Patta, Khasra-Khatauni) for online land ownership verification.",
            "te": "భూ యాజమాన్య ధృవీకరణ కోసం రాష్ట్ర భూ రికార్డులను (భూలేఖ్, పట్టా, పహానీ) అనుసంధానించే డిజిటల్ ఇండియా అధికారిక పోర్టల్.",
            "hi": "भूमि स्वामित्व सत्यापन के लिए राज्य के भू-अभिलेखों (भूलेख, खसरा-खतौनी) को जोड़ने वाला डिजिटल इंडिया आधिकारिक पोर्टल।"
        },
        "required_items": ["District, Tehsil, and Village Name", "Khasra Number / Survey Number / Owner Name"],
        "typical_steps": [
            {
                "title": "Open Digital India Land Records / State Bhulekh portal",
                "action": "Visit dilrmp.gov.in and click on your state link to access the state digital land registry.",
                "tip": "State portals (like Dharani, Bhulekh, AnyRoR, Bhoomi) are all verified under the National Portal.",
                "simplified": "Open the official government land records website and choose your state."
            },
            {
                "title": "Select your District, Tehsil/Mandal, and Village",
                "action": "Use the dropdown menus to choose the exact administrative location where your land is situated.",
                "tip": "Refer to previous property tax receipts for the correct village revenue name.",
                "simplified": "Choose your district, mandal, and village name from the list."
            },
            {
                "title": "Enter Survey Number or Owner Name",
                "action": "Type the land Survey Number, Khasra Number, or registered Owner Name to search records.",
                "tip": "Search by Survey/Khasra number is the fastest and most accurate.",
                "simplified": "Type the survey number or property owner name into the search box."
            },
            {
                "title": "View and download verified Record of Rights (ROR / Patta)",
                "action": "Inspect the digital land passbook, ownership details, and survey map, and print the verified copy.",
                "tip": "Digital land records from official state portals are legally recognized proof of ownership.",
                "simplified": "Check your land details and save or print your digital land ownership paper."
            }
        ]
    },

    # 16. Agriculture, Rural & Environment -> PM-KISAN Samman Nidhi
    {
        "service_id": "pm_kisan_samman",
        "service_name": {
            "en": "PM-KISAN Samman Nidhi Official Portal",
            "te": "పీఎం కిసాన్ సమ్మాన్ నిధి పోర్టల్",
            "hi": "पीएम किसान सम्मान निधि आधिकारिक पोर्टल"
        },
        "category": "Agriculture, Rural & Environment",
        "government_level": "Central",
        "department": "Department of Agriculture and Farmers Welfare, Ministry of Agriculture",
        "official_url": "https://pmkisan.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/agriculture-rural-environment",
        "keywords": [
            "farmer scheme", "pm kisan", "kisan samman nidhi", "farmer payment status",
            "pm kisan ekyc", "farmer benefit", "kisan portal", "farmer registration",
            "kisan installment", "farmer subsidy",
            "రైతు పథకం", "పీఎం కిసాన్", "రైతు భరోసా", "రైతు సహాయం", "కిసాన్ సమ్మాన్",
            "किसान योजना", "पीएम किसान", "किसान सम्मान निधि", "किसान ईकेवाईसी", "किसान भुगतान स्थिति"
        ],
        "aliases": [
            "PM-KISAN", "Kisan Samman Nidhi", "Farmer Scheme", "PM Kisan Beneficiary Status",
            "Farmer eKYC Portal", "PM Kisan Installment"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "passport"
        ],
        "description": {
            "en": "Official Government of India portal for the PM-KISAN scheme providing direct income support of ₹6,000 per year to small and marginal farmer families.",
            "te": "రైతు కుటుంబాలకు ఏటా ₹6,000 ప్రత్యక్ష ఆదాయ సహాయాన్ని అందించే పీఎం-కిసాన్ పథకం అధికారిక కేంద్ర ప్రభుత్వ పోర్టల్.",
            "hi": "किसान परिवारों को प्रति वर्ष ₹6,000 की प्रत्यक्ष आय सहायता प्रदान करने वाला पीएम-किसान योजना का आधिकारिक पोर्टल।"
        },
        "required_items": ["Aadhaar Card", "Land Ownership Documents (Khasra/Patta)", "Bank Account Details"],
        "typical_steps": [
            {
                "title": "Open the official PM-KISAN portal",
                "action": "Visit pmkisan.gov.in. Verify that the address ends with '.gov.in'.",
                "tip": "Look for the 'Farmers Corner' section on the homepage.",
                "simplified": "Open the official government PM-KISAN website by clicking the link."
            },
            {
                "title": "Check Beneficiary Status or Complete e-KYC",
                "action": "Click on 'Beneficiary Status' to check installment deposits, or 'e-KYC' to complete mandatory verification.",
                "tip": "e-KYC can be completed in 1 minute using your Aadhaar OTP on the website.",
                "simplified": "Click 'Beneficiary Status' to see your payment or 'eKYC' to verify your Aadhaar."
            },
            {
                "title": "Enter your Aadhaar or Registration Number",
                "action": "Type your 12-digit Aadhaar number or PM-KISAN registration ID and enter the captcha code.",
                "tip": "If you don't know your registration number, click 'Know Your Registration Number'.",
                "simplified": "Type your Aadhaar number to view your farmer payment record."
            },
            {
                "title": "Review installment deposit details",
                "action": "Check the status of ₹2,000 quarterly installments credited directly to your bank account via PFMS.",
                "tip": "If payments are pending, check if bank account seeding with Aadhaar is complete.",
                "simplified": "See the dates and amounts deposited into your bank account."
            }
        ]
    },

    # 17. Health & Wellness -> Online Registration System (ORS Hospital Appointment)
    {
        "service_id": "ors_hospital_appointment",
        "service_name": {
            "en": "Online Registration System (ORS Hospital Appointment)",
            "te": "ఆన్‌లైన్ రిజిస్ట్రేషన్ సిస్టమ్ (ORS ఆసుపత్రి అపాయింట్‌మెంట్)",
            "hi": "ऑनलाइन पंजीकरण प्रणाली (ORS अस्पताल अपॉइंटमेंट)"
        },
        "category": "Health & Wellness",
        "government_level": "Central",
        "department": "Ministry of Health and Family Welfare / National Informatics Centre (NIC)",
        "official_url": "https://ors.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/health-wellness",
        "keywords": [
            "hospital appointment", "doctor consultation", "online doctor", "aiims appointment",
            "ors patient portal", "opd appointment", "government hospital booking",
            "book doctor", "hospital opd", "health appointment", "medical consultation",
            "డాక్టర్ అపాయింట్‌మెంట్", "ఆసుపత్రి", "ఓపీడీ", "వైద్యుడు", "ఎయిమ్స్ అపాయింట్‌మెంట్",
            "डॉक्टर अपॉइंटमेंट", "अस्पताल", "ओपीडी बुकिंग", "सरकारी अस्पताल", "एम्स अपॉइंटमेंट", "डॉक्टर सलाह"
        ],
        "aliases": [
            "ORS Patient Portal", "Hospital Appointment", "AIIMS OPD Booking",
            "Online Doctor Appointment", "Govt Hospital OPD Booking", "ORS Gov In"
        ],
        "negative_keywords": [
            "scholarship", "driving", "passport", "ration", "caste", "land", "tax", "pf", "epfo"
        ],
        "description": {
            "en": "Official Government of India portal for booking OPD appointments at AIIMS, Central Government hospitals, and major public medical institutions.",
            "te": "ఎయిమ్స్ మరియు ప్రధాన కేంద్ర ప్రభుత్వ ఆసుపత్రులలో OPD అపాయింట్‌మెంట్‌లను బుక్ చేయడానికి భారత ప్రభుత్వ అధికారిక పోర్టల్.",
            "hi": "एम्स और प्रमुख केंद्र सरकार के अस्पतालों में ओपीडी अपॉइंटमेंट बुक करने का आधिकारिक सरकारी पोर्टल।"
        },
        "required_items": ["Aadhaar or Mobile Number", "Patient Name and Age Details"],
        "typical_steps": [
            {
                "title": "Open the ORS Hospital Portal",
                "action": "Open the official government patient registration website (ors.gov.in).",
                "tip": "Look for the button that says 'Book Appointment Now'.",
                "simplified": "Open the hospital website by clicking the link. Look for the 'Book Appointment' button."
            },
            {
                "title": "Choose your hospital and department",
                "action": "Select your city or state, choose the hospital (e.g. AIIMS), and pick the clinic department (e.g. General Medicine, Eye, Cardiology).",
                "tip": "If unsure of the department, 'General Medicine' is the best starting choice.",
                "simplified": "Pick the hospital near you and choose the type of doctor you want to see."
            },
            {
                "title": "Select a convenient date",
                "action": "A calendar will show green dates that have open slots. Click on the day that suits you.",
                "tip": "Green slots are available. Red slots are already booked.",
                "simplified": "Look at the calendar and click on any green date that is convenient for you."
            },
            {
                "title": "Verify with your mobile number",
                "action": "Enter your mobile phone number. You will receive an SMS code on your phone to confirm.",
                "tip": "Enter the 6-digit code received on your phone to confirm your booking.",
                "simplified": "Type your phone number. You will get a text message with a code. Enter that code."
            },
            {
                "title": "Save your appointment slip",
                "action": "Download or write down your appointment slip number (UHID/Booking Ref).",
                "tip": "Take this slip or show the SMS on your phone when visiting the hospital counter.",
                "simplified": "Your appointment is confirmed! Note down the appointment number or take a photo of the screen."
            }
        ]
    },

    # 18. Justice, Law & Grievances -> CPGRAMS Public Grievance
    {
        "service_id": "cpgrams_grievance",
        "service_name": {
            "en": "CPGRAMS (Centralized Public Grievance Redress Portal)",
            "te": "CPGRAMS (కేంద్ర ప్రజా ఫిర్యాదుల పరిష్కార పోర్టల్)",
            "hi": "सीपीजीआरएएमएस (केंद्रीकृत लोक शिकायत निवारण पोर्टल)"
        },
        "category": "Justice, Law & Grievances",
        "government_level": "Central",
        "department": "Department of Administrative Reforms and Public Grievances (DARPG)",
        "official_url": "https://pgportal.gov.in/",
        "india_gov_reference": "https://www.india.gov.in/topics/justice-law-grievances",
        "keywords": [
            "grievance", "complaint to government", "pg portal", "cpgrams", "file complaint",
            "public grievance", "darpg", "lodge grievance", "government complaint", "complaint redress",
            "ప్రజా ఫిర్యాదు", "ఫిర్యాదుల పోర్టల్", "ప్రభుత్వానికి ఫిర్యాదు", "ఫిర్యాదు నమోదు",
            "लोक शिकायत", "शिकायत दर्ज करें", "पीजी पोर्टल", "सरकारी शिकायत", "सीपीजीआरएएमएस", "शिकायत निवारण"
        ],
        "aliases": [
            "CPGRAMS", "PG Portal", "Public Grievance", "Central Grievance Portal",
            "File Government Complaint", "DARPG Grievance"
        ],
        "negative_keywords": [
            "hospital", "doctor", "scholarship", "driving", "passport", "electricity", "ration"
        ],
        "description": {
            "en": "Official Government of India portal (CPGRAMS) for citizens to lodge grievances and complaints against Central and State Government departments with time-bound redressal.",
            "te": "కేంద్ర మరియు రాష్ట్ర ప్రభుత్వ శాఖలపై ఫిర్యాదులను నమోదు చేయడానికి మరియు గడువులోగా పరిష్కారం పొందడానికి పౌరుల కోసం అధికారిక పోర్టల్.",
            "hi": "केंद्र और राज्य सरकार के विभागों के खिलाफ शिकायतें दर्ज करने और समयबद्ध निवारण के लिए नागरिकों का आधिकारिक पोर्टल।"
        },
        "required_items": ["Mobile Number / Email ID", "Details of the Department and Nature of Grievance"],
        "typical_steps": [
            {
                "title": "Open the official CPGRAMS Public Grievance Portal",
                "action": "Visit pgportal.gov.in. Verify that the address ends with '.gov.in'.",
                "tip": "Click on 'Lodge Public Grievance' on the homepage.",
                "simplified": "Open the official government grievance website by clicking the link."
            },
            {
                "title": "Sign in or register your citizen account",
                "action": "Log in using your registered mobile number or complete a quick 1-minute registration.",
                "tip": "Citizens can also log in directly using MeriPehchan / JanParichay single sign-on.",
                "simplified": "Sign in with your mobile phone number and code."
            },
            {
                "title": "Select the Ministry, Department, or State Government",
                "action": "Choose the specific department your complaint relates to (for example: Banking, Railways, Pensions, or Posts).",
                "tip": "If unsure, choose the central ministry overseeing the subject.",
                "simplified": "Pick the government office or department your issue is about."
            },
            {
                "title": "Describe your grievance clearly and attach supporting papers",
                "action": "Type a plain explanation of what went wrong, previous complaint numbers (if any), and upload supporting PDF letters.",
                "tip": "Keep the explanation factual, respectful, and mention what specific relief you are requesting.",
                "simplified": "Write down what happened in simple words and attach any letters you have."
            },
            {
                "title": "Submit and track your unique Grievance Registration Number",
                "action": "Save the registration number sent by SMS. Departments are mandated to resolve grievances within 30 days.",
                "tip": "You will receive SMS notifications at every step of progress until resolution.",
                "simplified": "Submit your complaint and save your tracking number. You will receive updates by SMS."
            }
        ]
    }
]


def get_catalogue() -> List[Dict[str, Any]]:
    """Return the entire master service catalogue."""
    return GOVERNMENT_SERVICES_CATALOGUE


def get_service_by_id(service_id: str) -> Optional[Dict[str, Any]]:
    """Find a specific government service by unique ID."""
    for service in GOVERNMENT_SERVICES_CATALOGUE:
        if service["service_id"] == service_id:
            return service
    return None


def get_services_by_category(category: str) -> List[Dict[str, Any]]:
    """Return all services registered under an official India.gov.in category."""
    cat_lower = category.lower().strip()
    return [
        s for s in GOVERNMENT_SERVICES_CATALOGUE
        if s["category"].lower() == cat_lower
    ]


def register_service(service: Dict[str, Any]) -> None:
    """
    Safely expand or update the government service catalogue at runtime.
    Validates required schema fields before appending.
    """
    required_keys = ["service_id", "service_name", "category", "government_level", "official_url", "keywords"]
    for key in required_keys:
        if key not in service:
            raise ValueError(f"Cannot register government service: missing required field '{key}'")
            
    # Check if category is one of the official National Portal categories
    if service["category"] not in OFFICIAL_GOV_CATEGORIES:
        raise ValueError(f"Category '{service['category']}' is not one of the official 18 National Portal categories.")

    # Update if already exists, else append
    for idx, existing in enumerate(GOVERNMENT_SERVICES_CATALOGUE):
        if existing["service_id"] == service["service_id"]:
            GOVERNMENT_SERVICES_CATALOGUE[idx] = service
            return

    GOVERNMENT_SERVICES_CATALOGUE.append(service)
