class PromptEngine:
    def __init__(self, system_prompt='You are a helpful assistant.'):
        self.system_prompt = system_prompt
        self.history = []

    def generate(self, user_input, context=None):
        prompt = self.system_prompt + "\n"
        if context:
            prompt += f"Context: {context}\n"
        prompt += f"User: {user_input}\nAssistant: "
        return f"[Simulated Response for: '{user_input}']"

    def update_context(self, message):
        self.history.append(message)
