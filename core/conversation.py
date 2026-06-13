class ConversationMemory:
    """Gestiona el historial de la conversación para mantener el contexto."""
    
    def __init__(self):
        self.history = []
        self.system_prompt = None

    def set_system_prompt(self, prompt: str):
        """Define el prompt del sistema (el rol del experto) y reinicia el contexto de usuario."""
        self.system_prompt = {"role": "system", "content": prompt}
        self.clear_history()

    def add_user_message(self, content: str):
        self.history.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str):
        self.history.append({"role": "assistant", "content": content})

    def get_messages(self) -> list:
        """Devuelve la lista completa de mensajes (Sistema + Historial)."""
        messages = []
        if self.system_prompt:
            messages.append(self.system_prompt)
        messages.extend(self.history)
        return messages

    def clear_history(self):
        """Limpia el historial de la conversación, manteniendo el experto actual."""
        self.history = []