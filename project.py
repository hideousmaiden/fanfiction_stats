import telebot as tb
from telebot import types
import random

token = '1844329888:AAFjGK4wfbv74AE0FfpgHtJbAPH9Z_qTNMo'
bot = tb.TeleBot(token, parse_mode=None)
bot.set_webhook()

@bot.message_handler(commands=['start'])
def start(m):
    user_text = m.text
    user_id = m.chat.id
    mes = """Добро пожаловать в Сан-Франциско!
    Это проект по проге. Он заключается примерно в том, что я закраулила кучу фанфиков из Archive of Our Own и что-то с ними сделала.
    Бот может присылать сгенерированные обученной на этой модели превью фанфиков и графики. Больше он, собственно, ничего не может.

    Классический фанфик на ao3 состоит из вороха тегов и иногда небольшого куска текста, который должен заинтересовать читателя. Модель поняла эту идею, но насколько она заинтересовывает - ещё вопрос."""
    bot.send_message(user_id, mes)

@bot.message_handler(commands=['generate'])
def gener_start(m):
    user_text = m.text
    user_id = m.chat.id
    with open('voltron_snaps.txt', 'r', encoding='utf-8') as f:
        body = f.read().split('конец')
    mes = random.choice(body)
    bot.send_message(user_id, mes)

@bot.message_handler(commands=['stats'])
def stats(m):
    user_text = m.text
    user_id = m.chat.id
    mes = 'Выберите на клавиатуре, какой график вам интересен:'
    keyb = types.ReplyKeyboardMarkup()
    for act in ['Возрастные ограничения', 'Типы взаимоотношений', 'Самые популярные пары',
    'Законченные vs незаконченные работы', 'Самые популярные персонажи', 'Распределение читательских оценок']:
        keyb.add(types.KeyboardButton(act))
    bot.send_message(user_id, mes, reply_markup=keyb)

@bot.message_handler(commands=['about'])
def about(m):
    user_text = m.text
    user_id = m.chat.id
    mes = 'Это всё нужно, чтобы получить оценку по проге. И научиться как-никак обучать модели'
    bot.send_message(user_id, mes)

@bot.message_handler(content_types=['text'])
def give_stat(m):
    user_text = m.text
    user_id = m.chat.id
    keyb = types.ReplyKeyboardRemove()
    convo = {'Возрастные ограничения':'v_age.jpeg', 'Типы взаимоотношений':'v_genre.jpeg', 'Самые популярные пары':'v_relationship.jpeg',
    'Законченные vs незаконченные работы':'v_complete.jpeg', 'Самые популярные персонажи':'v_character.jpeg',
    'Распределение читательских оценок':'v_popular.jpeg'}
    if user_text not in convo.keys():
        mes = 'Что-то вы не то шлёте, кажется'
        bot.send_message(user_id, mes, reply_markup=keyb)
    else:
        mes = 'вот:'
        bot.send_message(user_id, mes, reply_markup=keyb)
        fname = convo[user_text]
        bot.send_photo(user_id, open(fname, 'rb'))

bot.polling()
