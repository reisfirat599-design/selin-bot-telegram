import os
import telebot
from flask import Flask, request
from openai import OpenAI

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
RENDER_URL = "https://selin-bot-telegram.onrender.com"

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)
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
  bot.reply_to(message, "Merhaba! Ben Selin. Sana nasıl yardımcı olabilirim?")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
  user_message = message.text
  try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Sen yardımsever, samimi ve Türkçe konuşan bir asistansın.",
            },
            {"role": "user", "content": user_message},
        ],
    )
    bot_reply = response.choices[0].message.content
    bot.reply_to(message, bot_reply)
  except Exception as e:
    bot.reply_to(message, "Üzgünüm, bir hata oluştu.")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
