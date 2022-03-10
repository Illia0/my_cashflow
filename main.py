import telebot
import bdcore as bd
from telebot import types
import Audio

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
newprnameedit={}
whateditinnew={}

@bot.message_handler(commands=["start"])
def start(m, res=False):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Stonks"]
    keyboard.add(*buttons)
    bot.send_message(m.chat.id, bd.getstartmenu(str(m.from_user.id)), reply_markup=keyboard)
    bot.send_message(m.chat.id, bd.getAllactvieprojects(str(m.from_user.id)), reply_markup=keyboard)
    flags[str(m.from_user.id)] = 0


#flags: 1=name 2=description 3=category 4=cashflow 5="новые проекты" 6=twoclick 7=twoclickname 8=inputnnewedit
@bot.message_handler(content_types=["text"])
def handle_text(message):
    flag=flags.get(str(message.from_user.id),0)
    if flag == 1:
        crproject[str(message.from_user.id)]=projectC()
        crproject[str(message.from_user.id)].name=message.text.strip()
        bot.send_message(message.chat.id, "Опиши проект?")
        flags[str(message.from_user.id)] = 2
    elif flag == 2:
        crproject[str(message.from_user.id)].description=message.text.strip()
        bot.send_message(message.chat.id, "Из какой категории проект?")
        flags[str(message.from_user.id)] = 3
    elif flag == 3:
        crproject[str(message.from_user.id)].category=message.text.strip()
        bot.send_message(message.chat.id, "Ожидаемый cashflow?")
        flags[str(message.from_user.id)] = 4
    elif flag == 4:
        crproject[str(message.from_user.id)].cashflow=message.text.strip()
        crproject[str(message.from_user.id)].percent_complete = "0%"
        flags[str(message.from_user.id)] = 0
        bd.craetenewproject(str(message.from_user.id), crproject[str(message.from_user.id)])
        bot.send_message(message.chat.id, "Записал)\n/start")
    elif flag == 5:
        prname=bd.buttonnewprojects(str(message.from_user.id))
        for i in range(len(prname)):
            if prname[i]==message.text.strip():
                bot.send_message(message.chat.id,bd.getnewprdescription(str(message.from_user.id),prname[i]))
                newprnameedit[str(message.from_user.id)]=prname[i]
                flags[str(message.from_user.id)] = 6
    elif flag == 6:
        if newprnameedit[str(message.from_user.id)] == message.text.strip():
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["Название", "Категория", "cashflow","реализованость проекта","описание","выйти"]
            keyboard.add(*buttons)
            textm="что вы хотите изменить?\n"
            textm+=bd.getnewprojectbyname(str(message.from_user.id),newprnameedit[str(message.from_user.id)])
            textm+="\nописание:\n"
            textm+=bd.getnewprdescription(id,newprnameedit[str(message.from_user.id)])
            bot.send_message(message.chat.id, textm, reply_markup=keyboard)
            flags[str(message.from_user.id)] = 7
        else:
            prname = bd.buttonnewprojects(str(message.from_user.id))
            for i in range(len(prname)):
                if prname[i] == message.text.strip():
                    bot.send_message(message.chat.id, bd.getnewprdescription(str(message.from_user.id),prname[i]))
                    newprnameedit[str(message.from_user.id)] = prname[i]
                    flags[str(message.from_user.id)] = 6
    elif flag==7:
        prclass=bd.getnewprojectclassbyname(str(message.from_user.id), newprnameedit[str(message.from_user.id)])
        if message.text.strip() == "Название":
            text="Название сейчас: "+ prclass.name+'\n'
            bot.send_message(message.chat.id, text)
            whateditinnew[str(message.from_user.id)]="Название"
            flags[str(message.from_user.id)] = 8
        elif message.text.strip() == "Категория":
            text = "Категория сейчас: " + prclass.category + '\n'
            bot.send_message(message.chat.id, text)
            whateditinnew[str(message.from_user.id)] ="Категория"
            flags[str(message.from_user.id)] = 8
        elif message.text.strip() == "cashflow":
            text = "Cashflow сейчас: " + prclass.cashflow + '\n'
            bot.send_message(message.chat.id, text)
            whateditinnew[str(message.from_user.id)] = "cashflow"
            flags[str(message.from_user.id)] = 8
        elif message.text.strip() == "реализованость проекта":
            text = "реализованость проекта сейчас: " + prclass.percent_complete + '\n'
            bot.send_message(message.chat.id, text)
            whateditinnew[str(message.from_user.id)] = "реализованость проекта"
            flags[str(message.from_user.id)] = 8
        elif message.text.strip() == "описание":
            text = "описание сейчас: " + prclass.description + '\n'
            bot.send_message(message.chat.id, text)
            whateditinnew[str(message.from_user.id)] = "описание"
            flags[str(message.from_user.id)] = 8
        elif message.text.strip() == "выйти":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["Stonks"]
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, bd.getstartmenu(str(message.from_user.id)), reply_markup=keyboard)
            bot.send_message(message.chat.id, bd.getAllactvieprojects(str(message.from_user.id)), reply_markup=keyboard)
            flags[str(message.from_user.id)] = 0
    elif flag==8:
        pr = bd.getnewprojectclassbyname(str(message.from_user.id), newprnameedit[str(message.from_user.id)])
        if whateditinnew[str(message.from_user.id)] == "Название":
            pr.name = message.text.strip()
        elif whateditinnew[str(message.from_user.id)] == "Категория":
            pr.category = message.text.strip()
        elif whateditinnew[str(message.from_user.id)] == "cashflow":
            pr.cashflow = message.text.strip()
        elif whateditinnew[str(message.from_user.id)] == "реализованость проекта":
            pr.percent_complete = message.text.strip()
        elif whateditinnew[str(message.from_user.id)] == "описание":
            pr.description = message.text.strip()
        bd.editproject(str(message.from_user.id), "new", newprnameedit[str(message.from_user.id)], pr)
        flags[str(message.from_user.id)] = 0
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
    elif message.text.strip() == "новые \nпроекты":
        textm ="Выберите проект:\n" +  bd.getAllnewprojects(str(message.from_user.id))
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = bd.buttonnewprojects(str(message.from_user.id))
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, textm, reply_markup=keyboard)
        flags[str(message.from_user.id)] = 5
    elif message.text.strip() == 'Добавить проект':
        bot.send_message(message.chat.id, "Как назовем проект?", reply_markup=types.ReplyKeyboardRemove())
        flags[str(message.from_user.id)]=1

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    bot.reply_to(message, Audio.audio_handler(bot, message))


bot.polling(none_stop=True, interval=0)