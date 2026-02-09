def route_intent(intent_data):
    """
    Routes detected intent to system mode
    """
    intents = intent_data.get("intents", ["unknown"])
    intent = intents[0]

    if intent == "information":
        return "KNOWLEDGE_MODE"
    elif intent == "reminder":
        return "MEMORY_MODE"
    elif intent == "greeting":
        return "SOCIAL_MODE"
    else:
        return "DEFAULT_MODE"
