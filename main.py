import telebot
import bdcore as bd
from telebot import types

bot = telebot.TeleBot('5231795607:AAEx7PtuGz4MDSHf52R5nHl0VI6OAClets8')

class projectC:
    name=""
    category=""
    description=""
    percent_complete=""
    cashflow = ""
    def __init__(self):
        pass

flags={}
crproject={}

@bot.message_handler(commands=["start"])
def start(m, res=False):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Stonks"]
    keyboard.add(*buttons)
    bot.send_message(m.chat.id, bd.getstartmenu(str(m.from_user.id)), reply_markup=keyboard)
    bot.send_message(m.chat.id, bd.getAllactvieprojects(str(m.from_user.id)), reply_markup=keyboard)
    flags[str(m.from_user.id)] = 0


#flags: 1=name 2=description 3=category 4=cashflow 5=percent complete
@bot.message_handler(content_types=["text"])
def handle_text(message):
    flag=flags.get(str(message.from_user.id),0)
    if flag == 1:
        crproject[str(message.from_user.id)]=projectC()
        crproject[str(message.from_user.id)].name=message.text.strip()
        bot.send_message(message.chat.id, "Опиши проект?")
        flags[str(message.from_user.id)] = 2
    if flag == 2:
        crproject[str(message.from_user.id)].description=message.text.strip()
        bot.send_message(message.chat.id, "Из какой категории проект?")
        flags[str(message.from_user.id)] = 3
    if flag == 3:
        crproject[str(message.from_user.id)].category=message.text.strip()
        bot.send_message(message.chat.id, "Ожидаемый cashflow?")
        flags[str(message.from_user.id)] = 4
    if flag == 4:
        crproject[str(message.from_user.id)].cashflow=message.text.strip()
        crproject[str(message.from_user.id)].percent_complete = "0%"
        flags[str(message.from_user.id)] = 0
        bd.craetenewproject(str(message.from_user.id), crproject[str(message.from_user.id)])
        bot.send_message(message.chat.id, "Записал)\n/start")
    elif message.text.strip() == 'Stonks':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Добавить проект", "Редактировать проект","Взятся за резервы"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "Пора...", reply_markup=keyboard)
    elif message.text.strip() == 'Редактировать проект':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["реализованые \nпроекты","новые \nпроекты"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "и куда?", reply_markup=keyboard)
    elif message.text.strip() == "реализованые \nпроекты":
        textm ="Выберите проект:\n" +  bd.getAllactvieprojects(str(message.from_user.id))
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = bd.buttonprojects(str(message.from_user.id))
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, textm, reply_markup=keyboard)
    elif message.text.strip() == 'Добавить проект':
        bot.send_message(message.chat.id, "Как назовем проект?", reply_markup=types.ReplyKeyboardRemove())
        flags[str(message.from_user.id)]=1


bot.polling(none_stop=True, interval=0)