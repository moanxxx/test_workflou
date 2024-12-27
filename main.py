import telebot

# Замените "YOUR_BOT_TOKEN" на токен вашего бота, полученный у BotFather
BOT_TOKEN = "7738016274:AAG0ujQp7V0wtX_yCJ_0n9GpM9nXwvZd7U0"

bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это простой бот, который отвечает только на команду /start.")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен и готов к работе.")
    bot.infinity_polling()
