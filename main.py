import telebot
import os
import time

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот жив 🚀")

while True:
    try:
        bot.polling(non_stop=True, interval=0)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(10)
