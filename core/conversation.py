class ConversationMemory:
    """Gestiona el historial de la conversación para mantener el contexto por experto."""
    
    def __init__(self):
        self.histories = {}       # Diccionario de historiales: {rol: [mensajes]}
        self.system_prompts = {}   # Diccionario de system prompts: {rol: prompt_msg}
        self.active_role = None

    def set_system_prompt(self, role: str, prompt: str):
        """Define el prompt del sistema para el rol del experto y activa dicho rol."""
        self.active_role = role
        self.system_prompts[role] = {"role": "system", "content": prompt}
        if role not in self.histories:
            self.histories[role] = []

    def add_user_message(self, content: str):
        if self.active_role:
            self.histories[self.active_role].append({"role": "user", "content": content})

    def add_assistant_message(self, content: str):
        if self.active_role:
            self.histories[self.active_role].append({"role": "assistant", "content": content})

    def get_messages(self) -> list:
        """Devuelve la lista completa de mensajes (Sistema + Historial) del experto activo."""
        messages = []
        if self.active_role:
            sys_prompt = self.system_prompts.get(self.active_role)
            if sys_prompt:
                messages.append(sys_prompt)
            messages.extend(self.histories.get(self.active_role, []))
        return messages

    def clear_history(self):
        """Limpia el historial de la conversación del experto activo actualmente."""
        if self.active_role:
            self.histories[self.active_role] = []

    def pop_last_message(self):
        """Elimina el último mensaje del historial del experto activo (útil si la llamada al modelo falla)."""
        if self.active_role and self.histories.get(self.active_role):
            self.histories[self.active_role].pop()