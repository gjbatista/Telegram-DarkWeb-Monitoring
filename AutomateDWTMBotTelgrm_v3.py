# Código del script (AutomateDWTMBotTelgrm_v3.py)
import logging
import os
from requests_tor import RequestsTor
import bs4  # import BeautifulSoup for parsing
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configurar el registro (logging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Tu token de acceso de Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Define los sitios a monitorear
SITES_FILE = 'sites.txt'

# Variables globales para controlar la búsqueda
search_in_progress = False
results_summary = []

def read_sites_from_file(file_path):
    """Reads sites from a file and returns a list of tuples (name, url)."""
    sites = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, url = line.strip().split(maxsplit=1)
                sites.append((name, url))
    except Exception as e:
        logger.error(f"Error reading sites from file: {e}")
    return sites

async def send_telegram_message(bot, chat_id, message):
    """Send a message to a Telegram chat."""
    await bot.send_message(chat_id=chat_id, text=message)

async def scrape_and_search(url, keyword, bot, chat_id, total_sites, current_index):
    """Scrapes a .onion site and searches for a specified keyword."""
    global search_in_progress, results_summary
    if not search_in_progress:
        return

    try:
        # Initialize RequestsTor
        requests = RequestsTor(tor_ports=(9050,), tor_cport=9051)
        response = requests.get(url)  # No need to use proxies attribute

        response.raise_for_status()  # Check for HTTP errors

        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # Find all text content on the page
        text_content = soup.get_text()

        if keyword.lower() in text_content.lower():  # Case-insensitive search
            message = "Keyword '{}' found on {}".format(keyword, url)
            logger.info(message)
            await send_telegram_message(bot, chat_id, message)
            results_summary.append(message)

        # Calcular el porcentaje de progreso
        progress = (current
