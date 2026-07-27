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
  return "Kanal Bot is running!", 200


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  cta_mesaji = (
      "✨ GİRNE, MAĞUSA & LEFKOŞA REZERVASYON HATTI ✨\n\n"
      "Selam Canımlar! 💋\n"
      "Fiyatlar, kurallar, orijinal fotoğraflar ve randevu detayları için tek"
      " yapman gereken **hemen aşağıdaki butona tıklayıp botumla sohbeti"
      " başlatmak!** 👇\n\n"
      "🤖 Rezervasyon ve Bilgi İçin Tıkla:\n"
      "👉 @selin_kibris_bot\n\n"
      "📢 *Özel indirimlerden ve günlük paylaşımlardan anında haberdar olmak"
      " için ana kanalımıza katılmayı unutma:*\n"
      "👉 https://t.me/selin_kibris"
  )
  bot.reply_to(message, cta_mesaji, parse_mode="Markdown")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
  cta_mesaji = (
      "✨ GİRNE, MAĞUSA & LEFKOŞA REZERVASYON HATTI ✨\n\n"
      "Selam Canımlar! 💋\n"
      "Fiyatlar, kurallar, orijinal fotoğraflar ve randevu detayları için tek"
      " yapman gereken **hemen aşağıdaki butona tıklayıp botumla sohbeti"
      " başlatmak!** 👇\n\n"
      "🤖 Rezervasyon ve Bilgi İçin Tıkla:\n"
      "👉 @selin_kibris_bot\n\n"
      "📢 *Özel indirimlerden ve günlük paylaşımlardan anında haberdar olmak"
      " için ana kanalımıza katılmayı unutma:*\n"
      "👉 https://t.me/selin_kibris"
  )
  bot.reply_to(message, cta_mesaji, parse_mode="Markdown")


app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
