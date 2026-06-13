# Chatbot Multi-Experto Local (Ollama + Gemma3:1b)

Este proyecto implementa un chatbot de consola 100% offline que permite consultar a tres expertos diferentes (Software, Marketing, Legal) manteniendo el contexto de la conversación.

## Requisitos Previos
1. Instalar [Ollama](https://ollama.com/).
2. Descargar el modelo ejecutando en tu terminal: `ollama run gemma3:1b`
3. Instalar las dependencias de Python: `pip install -r requirements.txt`

## Ejecución
Ejecuta `python main.py` para iniciar la aplicación.

## Resolución de Problemas (Errores Comunes)

### 1. Error de conexión con Ollama
* **Mensaje esperado**: `[!] Error de conexión: Asegúrate de que la aplicación Ollama está iniciada en tu ordenador...`
* **Causa**: El servicio o aplicación de Ollama no está en ejecución en segundo plano.
* **Solución**: Inicia la aplicación de Ollama en tu sistema operativo o ejecuta `ollama serve` en una terminal antes de iniciar el chatbot.

### 2. Error de modelo no encontrado (404)
* **Mensaje esperado**: `[!] Error: El modelo 'gemma3:1b' no está disponible. Ejecuta 'ollama run gemma3:1b'...` o un diagnóstico de advertencia al inicio.
* **Causa**: Ollama está en ejecución, pero no se ha descargado localmente el modelo específico `gemma3:1b`.
* **Solución**: Abre una terminal y ejecuta el comando:
  ```bash
  ollama pull gemma3:1b
  ```
  Una vez completada la descarga, vuelve a ejecutar el chatbot.