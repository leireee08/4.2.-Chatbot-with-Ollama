import sys
from experts.expert_prompts import EXPERTS
from core.chatbot import LocalChatbot

def mostrar_menu_expertos():
    print("\n" + "="*55)
    print("🧠 SELECCIÓN DE EXPERTO TEMÁTICO")
    print("="*55)
    for key, data in EXPERTS.items():
        print(f"[{key}] {data['nombre']}")
    print("[0] Salir del programa")
    print("="*55)

def mostrar_descripcion_expertos():
    print("\n🌟 BIENVENIDO AL ASISTENTE MULTI-EXPERTO LOCAL 🌟")
    print("Este sistema te permite interactuar de forma 100% privada y offline con tres perfiles especializados:")
    print("  💻 1. Experto en Programación: Te ayuda a escribir, depurar, explicar y optimizar código de software.")
    print("  📈 2. Experto en Marketing: Diseña estrategias de crecimiento, redacta copies y sugiere métricas como ROI y KPIs.")
    print("  ⚖️ 3. Experto Jurídico-Legal: Redacta y analiza borradores de contratos y te orienta formalmente en derecho corporativo.")
    print("------------------------------------------------------------------------------------------------------")

def main():
    mostrar_descripcion_expertos()
    print("Iniciando sistema offline... Conectando con Ollama (gemma3:1b)")
    bot = LocalChatbot(model_name="gemma3:1b")
    
    # Comprobación de disponibilidad del modelo al iniciar
    status_info = bot.check_model_availability()
    if status_info["success"]:
        print("✅ ¡Conexión con Ollama exitosa! El modelo 'gemma3:1b' está listo para usar.")
    else:
        print("\n⚠️  [ATENCIÓN] No se pudo comprobar la disponibilidad del modelo.")
        print(f"Detalle: {status_info['error']}")
        print("Puedes continuar, pero es posible que las consultas fallen si Ollama o el modelo no están listos.\n")

    try:
        while True:
            mostrar_menu_expertos()
            try:
                opcion = input("Selecciona una opción: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\nApagando sistema de forma segura. ¡Hasta pronto!")
                sys.exit(0)
            
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
                        # Recordatorio del experto activo antes de cada turno
                        prompt_label = f"\n[{experto_actual['nombre']}] Tú: "
                        user_input = input(prompt_label).strip()
                        
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
                        print("\n\nApagando sistema de forma segura. ¡Hasta pronto!")
                        sys.exit(0)
                    except EOFError:
                        print("\n\nApagando sistema de forma segura. ¡Hasta pronto!")
                        sys.exit(0)
            else:
                print("\n[!] Opción no válida. Por favor, selecciona un número del menú.")
    except (KeyboardInterrupt, EOFError):
        print("\n\nApagando sistema de forma segura. ¡Hasta pronto!")
        sys.exit(0)

if __name__ == "__main__":
    main()