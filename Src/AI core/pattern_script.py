class PromptEngine:
    def generate(self, user_input, context=None):
        """
        Simple response generator (LLM placeholder)
        """
        response = f"AI Response to: {user_input}"

        if context:
            response += f"\n[Vision Context]: {context}"

        return response
