import telebot
import random
from telebot import types
import requests

# -*- coding: utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

bot = telebot.TeleBot("1408178896:AAH-IfABp-L9COzXVcBlX9GFxQM8JdYN1h0", parse_mode='HTML')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    gen_pass = types.KeyboardButton("Сгенерировать пароль")
    markup.add(gen_pass)

    # gen pass
    # passw = ''
    # for x in range(12):
    #     passw = passw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    #return

    bot.send_message(message.chat.id, "Нажми кнопочку".format(message.from_user, bot.get_me()), parse_mode='html',
                    reply_markup=markup)

@bot.message_handler(content_types=['text'])
def gen(message):
    if message.text == "Сгенерировать пароль":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        gen_pass = types.KeyboardButton("Сгенерировать пароль")
        markup.add(gen_pass)
        # gen pass
        passw = ''
        for x in range(12):
            passw = passw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        # return
        bot.send_message(message.chat.id, passw, parse_mode='html',
                         reply_markup=markup)

    if message.text == 'Конец':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        # gen pass
        # passw = ''
        # for x in range(12):
        #     passw = passw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        # return
        bot.send_message(message.chat.id, passw, parse_mode='html',
                         reply_markup=markup)

#RUN
bot.polling(none_stop=True)