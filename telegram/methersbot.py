import telebot 
import config
import keyboard
import random
import time
import os
from files.bot_funcs import *
from telebot import types

bot = telebot.TeleBot(config.TOKEN1)

@bot.message_handler(commands=['start', 'start_methers'])
def start(message):
    bot.send_message(message.chat.id, random.choice(config.hello))

@bot.message_handler(commands=['shutdown_123'])
def shutdown(message):
    os.system('shutdown/s')

@bot.message_handler(commands=['stop_bot123'])
def stop(message):
    keyboard.press_and_release('ctrl + c')

@bot.message_handler(commands=['start_smoking_test'])
def start_test(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    bt1 = types.KeyboardButton('Yup, im ready')
    bt2 = types.KeyboardButton('Oops, not now')    
    markup.add(bt1, bt2)
    bot.send_message(message.chat.id, 'Are you sure?', reply_markup=markup)   

@bot.message_handler(commands=['stupid_questions'])
def stupid_questions(message):

    markup = types.ReplyKeyboardMarkup(row_width=3)
    for i in config.questions:
        markup.add(types.KeyboardButton(i))
    bot.send_message(message.chat.id, 'Here you go...', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def reply(message):

    user_message = message.text.strip() 
    print(f'{message.from_user.first_name} {message.from_user.last_name}: {user_message}')

    if user_message == 'Yup, im ready':

        markup = types.ReplyKeyboardMarkup(row_width=3)
        age1 = types.KeyboardButton('my age is < 18')
        age2 = types.KeyboardButton('my age is => 18')
        markup.add(age1, age2)
        bot.send_message(message.chat.id, 'How old are you?', reply_markup = markup)

    elif 'my age' in user_message and '18' in user_message:

        global AGE
        AGE = user_message
        markup = types.ReplyKeyboardMarkup(row_width=3)
        pol1 = types.KeyboardButton('My gender is male')
        pol2 = types.KeyboardButton('My gender is female')
        markup.add(pol1, pol2)
        bot.send_message(message.chat.id, 'What is your sex?', reply_markup = markup)

    elif user_message == 'My gender is male' or user_message == 'My gender is female':

        sex = user_message
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, smoking_test_result(AGE, sex), reply_markup = markup)

    elif user_message == 'Oops, not now':
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Then what the fuck do you want?', reply_markup = markup)

    elif user_message in config.questions:

        answer = stupid_questions_reply(user_message)
        if type(answer) == list:
            for i in range(len(answer)):
                bot.send_message(message.chat.id, answer[i])
                time.sleep(0.8)
        else:
            bot.send_message(message.chat.id, answer)

    else:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Don\'t waste my time', reply_markup = markup)

bot.polling()