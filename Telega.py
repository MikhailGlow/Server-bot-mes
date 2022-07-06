import telebot

bot = telebot.TeleBot("5468093435:AAHl63kZ2gG6Uqxija0E0lYXmxEL-6-4bnk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text + ", nigger!")


bot.infinity_polling()
