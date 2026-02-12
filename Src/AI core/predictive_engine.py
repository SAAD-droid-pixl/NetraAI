def predict(vision_data: dict):
    obj = vision_data.get("object_detected")

    if obj == "Traffic Signal":
        return "Traffic light will turn Green in 10 seconds."

    elif obj == "Physics Book":
        return "Example problem available for better understanding."

    elif obj == "Tomato & Onion":
        return "Suggested Recipe: Simple Vegetable Curry."

    else:
        return "No prediction available."
