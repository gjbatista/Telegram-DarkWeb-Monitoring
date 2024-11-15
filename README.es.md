# DarkWebMonitoring Bot

![DWMB](https://github.com/user-attachments/assets/338434c8-b8c9-4b97-a235-db77e80e5701)


## Descripción
Bot de Telegram para monitoreo de palabras clave en sitios .onion. Utiliza `requests_tor` para realizar web scraping a través de la red Tor y envía notificaciones a través de Telegram.

## Requisitos

- Python 3.11 o superior
- Librerías Python: `requests_tor`, `beautifulsoup4`, `python-telegram-bot`

## Crear el Bot de Telegram
1. **Crear un nuevo bot con BotFather**
   * Abre Telegram y busca `@BotFather`.
   * Inicia una conversación con BotFather y envía el comando `/start`.
   * Envía el comando `/newbot` y sigue las instrucciones para crear un nuevo bot.
   * Guarda el token de acceso que BotFather te proporciona. Este token se utilizará en el archivo `.env`.

2. **Configurar el token del bot:**
   * > En el apartado de [Instalación](https://github.com/gjbatista/Telegram-DarkWeb-Monitoring/blob/main/README.md#instalaci%C3%B3n), paso 4 se detalla como configurar el token del bot.

## Instalación

1. **Clonar el repositorio:**

   ```sh
   git clone https://github.com/gjbatista/Telegram-DarkWeb-Monitoring.git
   cd Telegram-DarkWeb-Monitoring

2. **Crear y activar un entorno  virtual:**
    ```sh
   python3.11 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   .\venv\Scripts\activate  # En Windows
3. **Instalar las dependencias:**
   ```sh
   pip install -r requirements.txt
4. **Crear un archivo .env en el directorio del proyecto:**
   ```env
   TELEGRAM_BOT_TOKEN=TU_TELEGRAM_BOT_TOKEN
   #Reemplaza TU_TELEGRAM_BOT_TOKEN con el token que obtuviste del BotFather.
5. **Crear un archivo** sites.txt **en el directorio del proyecto:**
   El archivo debe contener los sitios .onion que deseas monitorear, en el siguiente formato:
   ```txt
   DarkForest http://example1.onion
   Ahmia http://example2.onion
   ASAPmail http://example3.onion
   CIA http://example4.onion
   owledge http://example5.onion
   InfoCon http://example6.onion
   CTemplar http://example7.onion
   Best http://example8.onion
   Black http://example9.onion
   Elude http://example10.onion

## Uso
1. **Ejecutar el scrip:**
   ```sh
   python3.11 AutomateDWTMBotTelgrm_v3.py
2. **Interacción con el bot:**
<p align="center"> <img width="460" height="300" src="https://github.com/user-attachments/assets/e02629f3-b8cd-43ca-87a9-9bcc39b97f75"> </p>

   * Usar `/start` para recibir un mensaje de bienvenida.
   * Usar `/search <keyword>` para buscar una palabra clave específica en los sitios configurados.
   * Usar `/stop` para detener una búsqueda en curso y recibir un resumen de los resultados hasta el momento.

## Consideraciones de Seguridad
1. **Uso de Variables de Entorno:**
   * Asegúrate de que tu token de acceso de Telegram esté almacenado en el archivo `.env` para evitar exponerlo en el código público.
2. **Validación de Datos de Entrada:**
   * La entrada del usuario `(keyword)` se utiliza directamente en las búsquedas. Asegúrate de que los datos de entrada sean validados y sanitizados para prevenir ataques de inyección o entradas maliciosas.
3. **Protección contra Ataques de Denegación de Servicio (DoS):**
   *Implementa límites de frecuencia para los comandos para evitar que el bot sea abusado por solicitudes excesivas. Esto se puede hacer rastreando las solicitudes por usuario y limitando la cantidad permitida en un período de tiempo determinado.

# **Disclaimer**
> Este proyecto se proporciona con fines educativos y de investigación. No se ofrece ninguna garantía sobre el funcionamiento del bot o la precisión de los resultados obtenidos. El uso de este bot para fines ilegales o no autorizados está estrictamente prohibido. Los autores del proyecto no se hacen responsables de ningún daño o consecuencia derivada del uso del bot.

