import telebot
import random
import keyboards
import receipts

API_TOKEN = "2112477829:AAEazBdM6NP3T2Kp9o3uOcLdLfw-n9qdavw"
chat_time = {}

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
@bot.message_handler(regexp="[пП][рР][иИ][вВ][еЕ]{0,}[тТ]?")
def handle_hello(message):
    reply = ["Привет!", "Добрый день!"][random.randint(0, 1)]
    chat_time[message.chat.id] = 'breakfast'
    bot.send_message(message.chat.id, reply, reply_markup=keyboards.main_markup())


@bot.message_handler(regexp=".*(дела).*")
def handle_how_are_you(message):
    reply = ["Отлично!", "Супер!", "Здорово!"][random.randint(0, 2)]
    bot.send_message(message.chat.id, reply, reply_markup=keyboards.main_markup())


@bot.message_handler(regexp="Что мне приготовить?")
@bot.message_handler(regexp="Выбрать другой приём пищи ↩")
def handle_how_are_you(message):
    reply = "Для какого приёма пищи тебе нужен рецепт?"
    bot.send_message(message.chat.id, reply, reply_markup=keyboards.time_markup())


@bot.message_handler(regexp="На завтрак 🥞")
@bot.message_handler(regexp="На обед 🍜")
@bot.message_handler(regexp="На ужин 🍲")
@bot.message_handler(regexp="Другой рецепт 🔄")
def handle_how_are_you(message):
    global chat_time
    aliases = {
        "На завтрак 🥞": "breakfast",
        "На обед 🍜": "lunch",
        "На ужин 🍲": "dinner",
        "Другой рецепт 🔄": chat_time[message.chat.id]
    }
    chat_time[message.chat.id] = aliases[message.text]
    index = random.randint(0, 6)
    reply = receipts.receipts[aliases[message.text]][index]
    bot.send_message(message.chat.id, reply, reply_markup=keyboards.receipt_markup(), parse_mode='Markdown')


bot.infinite_polling()