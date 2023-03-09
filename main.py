import telebot
from telebot import types
import json
import requests
# https://t.me/horoscope_testBot
bot = telebot.TeleBot('5981017496:AAF0oIVjBQJBfHjITj6asaJq0If0GEXThCQ')
def get_signs():
    signs = {
        'aries':'♈Овен' ,
        'taurus':'♉Телец' ,
        'virgo':'♍Дева' ,
        'gemini':'♊Близнецы',
        'cancer':'♋Рак',
        'leo':'♌Лев',
        'libra':'♎Весы',
        'scorpio':'♏Скорпион',
        'sagittarius':'♐Стрелец',
        'capricorn':'♑Козерог',
        'aquarius':'♒Водолей',
        'pisces':'♓Рыбы',
    }
    return signs
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('♈Овен')
    item2 = types.KeyboardButton('♉Телец')
    item3 = types.KeyboardButton('♊Близнецы')
    item4 = types.KeyboardButton('♋Рак')
    item5 = types.KeyboardButton('♌Лев')
    item6 = types.KeyboardButton('♍Дева')
    item7 = types.KeyboardButton('♎Весы')
    item8 = types.KeyboardButton('♏Скорпион')
    item9 = types.KeyboardButton('♐Стрелец')
    item10 = types.KeyboardButton('♑Козерог')
    item11= types.KeyboardButton('♒Водолей')
    item12= types.KeyboardButton('♓Рыбы')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
    bot.send_message(message.chat.id,'Привет, выбери какого ты знака задиака!', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    signs = get_signs()
    for sign in signs:
        if message.text == signs[sign]:
            
            api = (
                    'https://horoscopes.rambler.ru/api/front/v1/horoscope/today/' + sign + '/'

            )
            goroscope_data = json.loads(requests.get(api).text)
            date = goroscope_data['source']
            title = goroscope_data['h1']
            text = goroscope_data['text']
            bot.send_message (message.chat.id, f'{date}\n{title} \n{text}')
   


bot.polling(none_stop=True)
