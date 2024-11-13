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
        progress = (current_index + 1) / total_sites * 100
        progress_message = "Progreso: {:.2f}% ({}/{})".format(progress, current_index + 1, total_sites)
        await send_telegram_message(bot, chat_id, progress_message)

    except Exception as e:  # General exception for all request-related errors
        error_message = "Error scraping {}: {}".format(url, e)
        logger.error(error_message)
        await send_telegram_message(bot, chat_id, error_message)
        results_summary.append(error_message)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('¡Hola! Usa el comando /search <keyword> para buscar una palabra clave en los sitios configurados. Usa /stop para detener la búsqueda.')

async def search(update: Update, context: CallbackContext) -> None:
    global search_in_progress, results_summary
    if search_in_progress:
        await update.message.reply_text('Otra búsqueda está en curso. Por favor, usa /stop para detenerla antes de iniciar una nueva búsqueda.')
        return

    if context.args:
        keyword = context.args[0]
        bot = context.bot
        chat_id = update.effective_chat.id
        sites = read_sites_from_file(SITES_FILE)
        total_sites = len(sites)
        search_in_progress = True
        results_summary = []
        for current_index, (name, url) in enumerate(sites):
            if not search_in_progress:
                break
            message = "\n--- Scraping {} ---".format(name)
            logger.info(message)
            await send_telegram_message(bot, chat_id, message)
            await scrape_and_search(url, keyword, bot, chat_id, total_sites, current_index)
        search_in_progress = False
        summary_message = "Resumen de búsqueda:\n" + "\n".join(results_summary)
        await send_telegram_message(bot, chat_id, summary_message)
    else:
        await update.message.reply_text('Por favor, proporciona una palabra clave. Uso: /search <keyword>')

async def stop(update: Update, context: CallbackContext) -> None:
    global search_in_progress, results_summary
    if search_in_progress:
        search_in_progress = False
        summary_message = "La búsqueda ha sido detenida.\nResumen de búsqueda hasta el momento:\n" + "\n".join(results_summary)
        await update.message.reply_text(summary_message)
        logger.info("La búsqueda ha sido detenida por el usuario.")
    else:
        await update.message.reply_text('No hay ninguna búsqueda en curso para detener.')

def main():
    # Initialize the Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("search", search))
    application.add_handler(CommandHandler("stop", stop))

    # Start polling for updates
    application.run_polling()

if __name__ == "__main__":
    main()
