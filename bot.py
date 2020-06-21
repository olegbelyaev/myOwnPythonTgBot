import telebot
from telebot import types
from telebot.types import Message

TOKEN = '878350380:AAHqSNWtOXQvzESImpZmZSM5152r9YdypkE'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'There is no answer =(')


bot.polling(timeout=60)
