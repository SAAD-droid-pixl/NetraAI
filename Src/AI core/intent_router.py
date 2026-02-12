def detect_intent(user_input: str):
    text = user_input.lower()

    if "what" in text or "explain" in text:
        return "explanation"

    elif "help" in text:
        return "assistance"

    elif "next" in text or "predict" in text:
        return "prediction"

    else:
        return "general_query"
