import telebot

bot = telebot.TeleBot('5231795607:AAEx7PtuGz4MDSHf52R5nHl0VI6OAClets8')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

bot.polling()