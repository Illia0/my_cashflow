import telebot
import bdcore as bd
from telebot import types

bot = telebot.TeleBot('5231795607:AAEx7PtuGz4MDSHf52R5nHl0VI6OAClets8')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    #bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Stonks"]
    keyboard.add(*buttons)
    bot.send_message(m.chat.id, bd.getstartmenu(str(m.from_user.id)), reply_markup=keyboard)
    bd.editCashflow(str(m.from_user.id), 135)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Stonks':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Добавить проект", "Редактировать проект"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "123", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)