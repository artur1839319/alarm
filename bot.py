import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(
        message.chat.id,
        "⭐ Оплата 150 Stars прошла успешно! Premium активирован на 30 дней."
    )

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_message(
        message.chat.id,
        "Привет! Нажми синюю кнопку меню слева внизу, чтобы открыть Умный будильник ⏰"
    )

print("Бот запущен и ждёт оплаты...")
bot.infinity_polling(skip_pending=True)
