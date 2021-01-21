import telebot
import random
import telebot

passw = ''
for x in range(12):
    passw = passw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

bot = telebot.TeleBot("1408178896:AAHzV0tRWaBK9S-__Slk-89dXmilgYndIHo", parse_mode='HTML')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    gen_pass = types.KeyboardButton("Сгенерировать пароль")
    markup.add(gen_pass)

    #return
    bot.send_message(message.chat.id, "Нажми кнопку, чтобы получить пароль".format(message.from_user,  bot.get_me()), parse_mode='html',
                    reply_markup=markup)
    # gen pass
    passw = ''
    for x in range(12):
        passw = passw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


@bot.message_handler(content_types=['text'])
def routre(message):
    if message.text == "Сгенирировать пароль":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        pr1 = types.KeyboardButton(passw)
        markup.add(pr1)

        # gen pass
        passw = ''
        for x in range(12):
            passw = passw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        # return
        bot.send_message(message.chat.id, passw,  parse_mode='html', reply_markup=markup)


#RUN
bot.polling(none_stop=True)






#Backup
"""
import telebot
import random
from telebot import types

passw = ''
for x in range(12):
    passw = passw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

bot = telebot.TeleBot("1408178896:AAHzV0tRWaBK9S-__Slk-89dXmilgYndIHo", parse_mode='HTML')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    gen_pass = types.KeyboardButton("Сгенерировать пароль")
    markup.add(gen_pass)

    #return
    bot.send_message(message.chat.id, "Новый пароль: ".format(message.from_user,  bot.get_me()), parse_mode='html',
                    reply_markup=markup)

    # gen pass
    passw = ''
    for x in range(12):
        passw = passw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


@bot.message_handler(content_types=['text'])
def routre(message):
    if message.text == "Сгенирировать пароль":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        pr1 = types.KeyboardButton(passw)
        markup.add(pr1)

        bot.send_message(message.chat.id, passw.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


#RUN
bot.polling(none_stop=True)
"""