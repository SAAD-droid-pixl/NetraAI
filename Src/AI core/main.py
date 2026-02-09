from prompt_engine import PromptEngine
from pattern_script import detect_intent
from intent_router import route_intent
from vision_context import get_vision_context
from execution_manager import decide_execution
from network_manager import is_internet_available

def run_netra_ai(user_input):
    engine = PromptEngine()

    intent_data = detect_intent(user_input)
    mode = route_intent(intent_data)

    vision_context = get_vision_context()
    internet = is_internet_available()

    # Decide task type
    task_type = "heavy_reasoning" if mode == "KNOWLEDGE_MODE" else "basic_qa"

    execution = decide_execution(task_type, internet)

    response = engine.generate(
        user_input=f"[{execution}] {user_input}",
        context=vision_context
    )

    return {
        "mode": mode,
        "execution_layer": execution,
        "response": response
    }

if __name__ == "__main__":
    output = run_netra_ai("Explain this building")
    print(output)

