memory_log = []

def store_memory(user_input: str, result: str):
    memory_log.append({
        "input": user_input,
        "result": result
    })

def get_memory():
    return memory_log
