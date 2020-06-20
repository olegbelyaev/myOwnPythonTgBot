# -*- coding: utf-8 -*-
import cofig
import telebot
import parser

bot = telebot.TeleBot(cofig.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "version : 2.20")
    bot.send_message(message.chat.id, "created by oleg ggwp gang")

if __name__ == '__main__':
    bot.polling(none_stop=True)                     
