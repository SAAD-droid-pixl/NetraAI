def analyze_vision(mode: str):
    if mode == "urban":
        return {
            "environment": "City Street",
            "object_detected": "Traffic Signal",
            "status": "Red Light"
        }

    elif mode == "learning":
        return {
            "environment": "Study Desk",
            "object_detected": "Physics Book",
            "topic": "Newton's Laws"
        }

    elif mode == "cooking":
        return {
            "environment": "Kitchen",
            "object_detected": "Tomato & Onion",
            "dish_hint": "Vegetable Curry"
        }

    else:
        return {
            "environment": "Unknown",
            "object_detected": "Unknown"
        }
