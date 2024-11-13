# DarkWebMonitoring Bot

![DWMB](https://github.com/user-attachments/assets/338434c8-b8c9-4b97-a235-db77e80e5701)


## Description
Telegram bot for keyword monitoring on .onion sites. Use 'requests_tor' to perform web scraping through the Tor network and send notifications via Telegram.

## Requirements

- Python 3.11 o superior
- Python libraries: `requests_tor`, `beautifulsoup4`, `python-telegram-bot`

## Create the Telegram Bot
1. **Create a new bot with BotFather**
   * Open Telegram and search for '@BotFather'.
   * Start a conversation with BotFather and send the command '/start'.
   * Send the command '/newbot' and follow the instructions to create a new bot.
   * Save the access token that BotFather provides you. This token will be used in the '.env' file.

2. **Configure the bot token:**
   * > In the [Installation](https://github.com/gjbatista/Telegram-DarkWeb-Monitoring/blob/main/README.md#instalaci%C3%B3n) section, step 4 details how to configure the bot token.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/gjbatista/Telegram-DarkWeb-Monitoring.git
   cd Telegram-DarkWeb-Monitoring

2. **Create and activate a virtual environment:**
    ```sh
   python3.11 -m venv venv
   source venv/bin/activate  # On Linux/Mac
   .\venv\Scripts\activate  # On Windows
3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
4. **Create an .env file in the project directory:**
   ```env
   TELEGRAM_BOT_TOKEN=TU_TELEGRAM_BOT_TOKEN
   #Replaces TU_TELEGRAM_BOT_TOKEN with the token you got from BotFather.
5. **Create a file** sites.txt **in the project directory:**
   The file must contain the .onion sites you want to monitor, in the following format:
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

## Use
1. **Run the script:**
   ```sh
   python3.11 AutomateDWTMBotTelgrm_v3.py
2. **Interaction with the bot:**
<p align="center"> <img width="460" height="300" src="https://github.com/user-attachments/assets/e02629f3-b8cd-43ca-87a9-9bcc39b97f75"> </p>

   * Use `/start` to receive a welcome message.
   * Use `/search <keyword>` to search for a specific keyword on configured sites.
   * Use `/stop` to stop an ongoing search and receive a summary of the results so far.

## Safety Considerations
1. **Using Environment Variables:**
   * Make sure your Telegram access token is stored in the '.env' file to avoid exposing it in the public code.
2. **Input Data Validation:**
   * The user input '(keyword)' is used directly in searches. Ensure input data is validated and sanitized to prevent injection attacks or malicious inputs.
3. **Protection against Denial-of-Service (DoS) attacks:**
   *Implement rate caps for commands to prevent your bot from being abused by excessive requests. This can be done by tracking requests per user and limiting the amount allowed in a given period of time.

# **Disclaimer**
> This project is provided for educational and research purposes. No guarantee is made about the operation of the bot or the accuracy of the results obtained. The use of this bot for illegal or unauthorized purposes is strictly prohibited. The authors of the project are not responsible for any damage or consequences derived from the use of the bot.
