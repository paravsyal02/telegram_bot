import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Load environment variables
load_dotenv()

# Access your tokens from the .env file
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Define a function to fetch Bitcoin price from Gemini
def get_price(update: Update, context: CallbackContext) -> None:
    response = requests.get("https://api.gemini.com/v1/pubticker/btcusd")
    if response.status_code == 200:
        data = response.json()
        price = data['last']
        update.message.reply_text(f"The current Bitcoin price is ${price}")
    else:
        update.message.reply_text("Sorry, I couldn't fetch the price right now. Please try again later.")

# Define a start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Use /price to get the current Bitcoin price.')

# Main function to set up and run the bot
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", get_price))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

# Handle non-command messages (optional)
def handle_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I didn't understand that command. Try using /price.")

if __name__ == '__main__':
    main()
