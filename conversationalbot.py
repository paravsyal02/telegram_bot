import os
import google.generativeai as genai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot token
TELEGRAM_BOT_TOKEN2 = os.getenv("TELEGRAM_BOT_TOKEN2")

# Create the generation configuration for Google Generative AI
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Define the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Specify the model name
    generation_config=generation_config,
)

# Start a new chat session with an empty history
chat_session = model.start_chat(history=[])

# Function to get AI response from Google Generative AI
def get_ai_response(user_input):
    try:
        response = chat_session.send_message(user_input)
        return response.text
    except Exception as e:
        logger.error(f"Error getting AI response: {e}")
        return "Sorry, I couldn't process that request at the moment."

# Define start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I’m an AI-powered conversational bot. How can I assist you today?")

# Define message handler for incoming messages
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    ai_response = get_ai_response(user_message)
    update.message.reply_text(ai_response)

# Main function to set up the bot
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN2, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
