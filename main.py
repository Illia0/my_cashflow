import telebot
import bdcore as bd
from telebot import types

bot = telebot.TeleBot('5231795607:AAEx7PtuGz4MDSHf52R5nHl0VI6OAClets8')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Stonks"]
    keyboard.add(*buttons)
    bot.send_message(m.chat.id, bd.getstartmenu(str(m.from_user.id)), reply_markup=keyboard)
    bot.send_message(m.chat.id, bd.getAllactvieprojects(str(m.from_user.id)), reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Stonks':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Добавить проект", "Редактировать проект","Взятся за резервы"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "Пора...", reply_markup=keyboard)
    if message.text.strip() == 'Редактировать проект':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["реализованые \nпроекты","новые \nпроекты"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "и куда?", reply_markup=keyboard)
    if message.text.strip() == "реализованые \nпроекты":
        textm ="Выберите проект:\n" +  bd.getAllactvieprojects(str(message.from_user.id))
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = bd.buttonprojects(str(message.from_user.id))
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, textm, reply_markup=keyboard)
    if message.text.strip() == 'Добавить проект':
        bot.send_message(message.chat.id, "Как назовем проект?", reply_markup=types.ReplyKeyboardRemove())

bot.polling(none_stop=True, interval=0)