import telebot
from telebot import types

bot = telebot.TeleBot('6705328771:AAGqDyAB_rWyLPRVJKcEiSEwDlRjuGy7LF8')

@bot.message_handler(commands=['hi'])
def start(message):
    mess = f'Hello, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['website']) #кнопка 2
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Watch Guide", url ="https://www.youtube.com/watch?v=I6G3MuSbbu4"))
    bot.send_message(message.chat.id, "Guide", reply_markup=markup)

@bot.message_handler(commands=['wallstreet'])  #кнопка 3
def wallstreet(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Watch Guide", url ="https://www.youtube.com/watch?v=0DeISvHMh4I"))
    bot.send_message(message.chat.id, "Guide", reply_markup=markup)

@bot.message_handler(commands=['support'])  #кнопка 4
def support(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Support chat", url="https://t.me/+JlIgMS-O8xA4N2Ji"))
    bot.send_message(message.chat.id, "Support", reply_markup=markup)

@bot.message_handler(commands=['satur'])  #кнопка 1
def satur(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit site", url ="https://explorer.nymtech.net/network-components/mixnode/1092"))
    bot.send_message(message.chat.id, "Site", reply_markup=markup)

@bot.message_handler(commands=['unique'])  #кнопка 2
def unique(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Visit site", url ="https://explorer.nymtech.net/network-components/mixnode/1176"))
    bot.send_message(message.chat.id, "Site", reply_markup=markup)



@bot.message_handler(commands=['start'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    satur = types.KeyboardButton("💻 Best node saturation")
    unique = types.KeyboardButton("🌍 Unique nodes")
    nodes = types.KeyboardButton("⚙️ Node guide")
    wallstreet = types.KeyboardButton("⚙️ Staking guide")
    support = types.KeyboardButton("🧑‍🔬 Online support")
    tracking = types.KeyboardButton("👀 Monitoring")

    markup.add(satur, unique, nodes, wallstreet, support, tracking)
    mess = f'Hello, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "⚙️ Node guide"):
        website(message)
    elif(message.text == "⚙️ Staking guide"):
        wallstreet(message)
    elif(message.text == "🌍 Unique nodes"):
        unique(message)
    elif(message.text == "🧑‍🔬 Online support"):
        support(message)
    elif(message.text == "💻 Best node saturation"):
        satur(message)
    elif (message.text == "👀 Monitoring"):
        bot.send_message(message.chat.id, text="Coming soon...")
    else:
        bot.send_message(message.chat.id, text="I don't understand you,bro! Choose another command")






bot.polling(none_stop=True)
