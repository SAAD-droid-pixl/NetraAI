from prompt_engine import PromptEngine
from pattern_script import detect_intent
from intent_router import route_intent
from vision_context import get_vision_context
from memory_manager import MemoryManager
from response_formatter import format_for_ar


def run_netra_ai(user_input):
    engine = PromptEngine()
    memory = MemoryManager()

    # Step 1: Detect intent
    intent_data = detect_intent(user_input)

    # Step 2: Route intent
    mode = route_intent(intent_data)

    # Step 3: Get vision context
    vision_context = get_vision_context()

    # Step 4: Generate AI response
    response = engine.generate(user_input, vision_context)

    # Step 5: Store memory (if needed)
    if mode == "MEMORY_MODE":
        memory.store(user_input)

    # Step 6: Format for AR display
    ar_response = format_for_ar(response)

    return {
        "mode": mode,
        "vision_context": vision_context,
        "response": ar_response
    }


# --- Test Run ---
if __name__ == "__main__":
    user_text = "What is this?"
    output = run_netra_ai(user_text)

    print("Mode:", output["mode"])
    print("Context:", output["vision_context"])
    print("AR Response:", output["response"])
