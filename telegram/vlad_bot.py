import telebot
import config


bot = telebot.TeleBot(config.TOKEN2)


@bot.message_handler(commands=['start_vlad', 'start'])
def start_handler(message):
	bot.send_message(message.chat.id, 'Опа')

@bot.message_handler(content_type=['text'])
def answer(message):
    print(f'{message.from_user.first_name} {message.from_user.last_name}: {user_message}')



bot.polling()