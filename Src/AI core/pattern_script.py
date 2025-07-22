# pattern_script.py

def detect_pattern(user_input):
    patterns = {
        "reminder": ["याद दिलाओ", "मुझे याद रखना", "मुझे याद दिलाना"],
        "information": ["यह क्या है", "जानकारी दो", "बताओ"],
        "greeting": ["नमस्ते", "हैलो", "कैसे हो"]
    }
    for intent, keywords in patterns.items():
        for word in keywords:
            if word in user_input:
                return f"Pattern Detected: {intent}"
    return "कोई पैटर्न नहीं मिला"
