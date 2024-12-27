
import os
import telebot

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Токен бота не найден. Убедитесь, что BOT_TOKEN добавлен в Secrets.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это простой бот, который отвечает только на команду /start.")

if __name__ == "__main__":
    print("Бот запущен и готов к работе.")
    bot.infinity_polling()

    #for commit1
