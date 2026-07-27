import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
RENDER_URL = "https://selin-bot-telegram.onrender.com"

bot = telebot.TeleBot(TOKEN)
app = Flask("selinbot")

bot.remove_webhook()
bot.set_webhook(url=RENDER_URL)


@app.route("/", methods=["POST"])
def getMessage():
  json_string = request.get_data().decode("utf-8")
  update = telebot.types.Update.de_json(json_string)
  bot.process_new_updates([update])
  return "!", 200


@app.route("/")
def webhook():
  return "Selin Bot is running!", 200


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  bot.reply_to(message, "Merhaba! Ben Selin. Şu an bakımdayım, çok yakında döneceğim!")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
  bot.reply_to(
      message,
      "Şu an geçici olarak bakımdayım, OpenAI bakiyem güncelleniyor. Çok yakında tekrar sohbet edeceğiz! 😊",
  )


app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
