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
  tanitim_mesaji = (
      "Selam Canım\n"
      "Girne merkez, Magusa ve Lefkoşa’da görüşme yapıyorum.\n"
      "Kendi yerim var\n"
      "Eve ve otele geliyorum (taksi ücreti size ait )\n"
      "Fotoğraflar Orijinal✅\n"
      "Kondom şart ✅\n"
      "Anal Yok-Ön Sevişme ✅\n"
      "Otel-Ev (Gecelik)✅\n"
      "Kendi Yerim var ✅\n\n"
      "Seans 6.000TL🇹🇷\n"
      "1 saat  11.000 TL🇹🇷\n"
      "3 saat  15.000 TL 🇹🇷 \n"
      "Gecelik 25.000 TL🇹🇷\n\n"
      "RESİMLER  HİKAYEMİZDE MEVCUT\n\n"
      "TELEGRAM KANALIMA ÜCRETSİZ KATILIP İNDİRİMLERDEN FAYDALANABİLİRSİNİZ\n\n"
      "👇                                   👇\n\n"
      "https://t.me/selin_kibris"
  )
  bot.reply_to(message, tanitim_mesaji)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
  tanitim_mesaji = (
      "Selam Canım\n"
      "Girne merkez, Magusa ve Lefkoşa’da görüşme yapıyorum.\n"
      "Kendi yerim var\n"
      "Eve ve otele geliyorum (taksi ücreti size ait )\n"
      "Fotoğraflar Orijinal✅\n"
      "Kondom şart ✅\n"
      "Anal Yok-Ön Sevişme ✅\n"
      "Otel-Ev (Gecelik)✅\n"
      "Kendi Yerim var ✅\n\n"
      "Seans 6.000TL🇹🇷\n"
      "1 saat  11.000 TL🇹🇷\n"
      "3 saat  15.000 TL 🇹🇷 \n"
      "Gecelik 25.000 TL🇹🇷\n\n"
      "RESİMLER  HİKAYEMİZDE MEVCUT\n\n"
      "TELEGRAM KANALIMA ÜCRETSİZ KATILIP İNDİRİMLERDEN FAYDALANABİLİRSİNİZ\n\n"
      "👇                                   👇\n\n"
      "https://t.me/selin_kibris"
  )
  bot.reply_to(message, tanitim_mesaji)


app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
