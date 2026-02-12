def execute(intent: str, vision_data: dict, prediction: str):

    return (
        f"🧠 Intent: {intent}\n"
        f"👁 Environment: {vision_data.get('environment')}\n"
        f"🎯 Detected: {vision_data.get('object_detected')}\n"
        f"🔮 Prediction: {prediction}"
    )
