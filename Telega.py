import telebot, json, vk_api
from telebot import types

vk_session = vk_api.VkApi('login', 'password')

client = telebot.TeleBot("5468093435:AAHl63kZ2gG6Uqxija0E0lYXmxEL-6-4bnk", parse_mode=None)

@client.message_handler(commands=["vk"])
def vk(message):
	rmk = types.ReplyKeyboardMarkup()
	rmk.add(types.KeyboardButton("Yes"), types.KeyboardButton("No"))
	msg = client.send_message(message.chat.id, "Wanna change your vk status?", reply_markup=rmk)
	client.register_next_step_handler(msg, vkUserAnswer)

def vkUserAnswer(message):
	if message.text == "Yes":
		msg = client.send_message(message.chat.id, "Write status:")
		client.register_next_step_handler(msg, vkChangeStatus)

def vkChangeStatus(message):
	vk_session.auth()
	vk = vk_session.get_api()
	vk.status.set(text=message.text)

client.polling()

#
# def writeJson(data={}):
# 	with open(f"test.json", "w", encoding="utf-8-sig") as file:
# 		json.dump(data, file, indent=4, ensure_ascii=False)
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# 	name = "Steve"
# 	name = message.chat.id
# 	data = {
# 		"Name": message.from_user.id
# 	}
# 	writeJson(data)
#
# @bot.message_handler(commands=['vk'])
# def vkChangeStatus(message):
#
#
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text + ", nigger!")
#
