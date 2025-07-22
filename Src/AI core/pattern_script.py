def detect_pattern(user_input):
    patterns = {
        "reminder": ["remind me", "remember for me", "give me a reminder"],
        "information": ["what is this", "give information", "tell me"],
        "greeting": ["hello", "hi", "how are you"]
    }
    for intent, keywords in patterns.items():
        for word in keywords:
            if word in user_input:
                return f"Pattern Detected: {intent}"
    return "No pattern found"
