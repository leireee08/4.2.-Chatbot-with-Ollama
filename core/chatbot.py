import ollama
from core.conversation import ConversationMemory

class LocalChatbot:
    """Clase principal que maneja la comunicación offline con Ollama."""
    
    def __init__(self, model_name="gemma3:1b"):
        self.model_name = model_name
        self.memory = ConversationMemory()
        self.client = ollama.Client() # Conexión al localhost por defecto

    def change_expert(self, expert_data: dict):
        """Cambia el experto y actualiza el prompt del sistema."""
        self.memory.set_system_prompt(expert_data["prompt"])
        
    def reset_conversation(self):
        """Reinicia el historial actual."""
        self.memory.clear_history()

    def ask(self, user_input: str) -> str:
        """Envía el mensaje al modelo local y gestiona los errores de conexión."""
        self.memory.add_user_message(user_input)
        
        try:
            # Llamada al modelo local usando el SDK de Ollama
            response = self.client.chat(
                model=self.model_name,
                messages=self.memory.get_messages(),
                stream=False # Modo síncrono para CLI simple
            )
            
            ai_message = response['message']['content']
            self.memory.add_assistant_message(ai_message)
            return ai_message
            
        except ollama.ResponseError as e:
            # Error si el modelo no está descargado
            self.memory.history.pop() # Quitamos el mensaje que falló
            if e.status_code == 404:
                return f"[!] Error: El modelo '{self.model_name}' no está disponible. Ejecuta 'ollama run {self.model_name}' en tu terminal."
            return f"[!] Error del modelo: {str(e)}"
            
        except Exception as e:
            # Error si el servicio Ollama no está corriendo (conexión offline fallida)
            self.memory.history.pop()
            return f"[!] Error de conexión: Asegúrate de que la aplicación Ollama está iniciada en tu ordenador.\nDetalles: {str(e)}"