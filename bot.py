# -*- coding: utf-8 -*-
import telebot
token = '878350380:AAHqSNWtOXQvzESImpZmZSM5152r9YdypkE'
bot = telebot.TeleBot(token)
bot.send_message(500283434, "hey, it's version : 2.20")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "version : 2.20")
    bot.send_message(message.chat.id, "created by oleg ggwp gang")

bot.polling(none_stop=False, interval=0, timeout=20)                   
