# Telegram Bot Project

This repository contains two Telegram bots:
1. **Bitcoin Price Bot (`bot.py`)** - Fetches real-time Bitcoin value.
2. **AI Chatbot (`conversationalbot.py`)** - Uses Google Gemini AI to enable interactive conversations.

---

## 📌 Features
### 1️⃣ Bitcoin Price Bot (`bot.py`)
- Fetches the current Bitcoin price in real-time.
- Provides instant updates when requested by a user.

### 2️⃣ AI Chatbot (`conversationalbot.py`)
- Uses **Google Gemini AI** for natural conversation.
- Can respond intelligently to various user queries.

---

## 🚀 Setup and Installation

### Prerequisites
- Python 3.x installed
- A Telegram bot token (from [@BotFather](https://t.me/botfather))
- API access for Bitcoin price data (if required)
- Google Gemini AI API key (for AI chatbot)

### Installation Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/paravsyal02/telegram_bot.git
   cd telegram_bot
   ```
2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables**
   Create a `.env` file and add:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   GEMINI_API_KEY=your_google_gemini_api_key
   ```
4. **Run the Bots**
   - Start Bitcoin Price Bot:
     ```sh
     python bot.py
     ```
   - Start AI Chatbot:
     ```sh
     python conversationalbot.py
     ```

---

## 📜 Usage
- **Bitcoin Bot**: Send a command (e.g., `/price`) to get the latest Bitcoin value.
- **AI Chatbot**: Start chatting with the bot, and it will respond using Google Gemini AI.

---

## 🛠 Future Enhancements
- ✅ Add support for multiple cryptocurrencies.
- ✅ Enhance AI chatbot with more advanced NLP features.
- ✅ Implement database support for chat history.

---

## 📩 Contributions
Feel free to fork this repository, open issues, or submit pull requests! 🎉

---

## 📜 License
This project is licensed under the **MIT License**.

---

### 🔗 Connect with Me
- GitHub: [@paravsyal02](https://github.com/paravsyal02)

