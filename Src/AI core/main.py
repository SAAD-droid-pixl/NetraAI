from vision_context import analyze_vision
from intent_router import detect_intent
from predictive_engine import predict
from memory_manager import store_memory
from execution_manager import execute


def run_simulation(mode: str, user_input: str):

    vision_data = analyze_vision(mode)
    intent = detect_intent(user_input)
    prediction = predict(vision_data)

    result = execute(intent, vision_data, prediction)

    store_memory(user_input, result)

    return result
