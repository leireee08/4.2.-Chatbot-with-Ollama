import sys
from experts.expert_prompts import EXPERTS
from core.chatbot import LocalChatbot

def mostrar_menu_expertos():
    print("\n" + "="*50)
    print("🧠 SELECCIÓN DE EXPERTO TEMÁTICO")
    print("="*50)
    for key, data in EXPERTS.items():
        print(f"[{key}] {data['nombre']}")
    print("[0] Salir del programa")
    print("="*50)

def main():
    print("Iniciando sistema offline... Conectando con Ollama (gemma3:1b)")
    bot = LocalChatbot(model_name="gemma3:1b")
    
    while True:
        mostrar_menu_expertos()
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "0":
            print("\nApagando sistema. ¡Hasta pronto!")
            sys.exit(0)
            
        if opcion in EXPERTS:
            experto_actual = EXPERTS[opcion]
            bot.change_expert(experto_actual)
            print(f"\n✅ Conectado con: {experto_actual['nombre']}")
            print("📝 Comandos disponibles: '/cambiar' (cambiar experto), '/reiniciar' (limpiar historial), '/salir' (salir)")
            print("-" * 60)
            
            # Bucle de conversación con el experto
            while True:
                try:
                    user_input = input("\nTú: ").strip()
                    
                    if not user_input:
                        continue
                        
                    if user_input.lower() == "/salir":
                        print("\nApagando sistema. ¡Hasta pronto!")
                        sys.exit(0)
                        
                    if user_input.lower() == "/cambiar":
                        print("\nSaliendo de la sala del experto...")
                        break # Rompe el bucle interno y vuelve al menú principal
                        
                    if user_input.lower() == "/reiniciar":
                        bot.reset_conversation()
                        print(f"\n[Sistema] Historial borrado. {experto_actual['nombre']} está listo para un nuevo tema.")
                        continue

                    # Consultar al modelo local
                    print(f"\n{experto_actual['nombre']} está escribiendo...")
                    respuesta = bot.ask(user_input)
                    print(f"\n[{experto_actual['nombre']}]:\n{respuesta}")
                    print("-" * 60)
                    
                except KeyboardInterrupt:
                    print("\n\nSaliendo del programa...")
                    sys.exit(0)
                except EOFError:
                    sys.exit(0)
        else:
            print("\n[!] Opción no válida. Por favor, selecciona un número del menú.")

if __name__ == "__main__":
    main()