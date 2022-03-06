import bdcore as bd

def add_idea(bot, message):
    bot.register_next_step_handler(message,find_text)
    obj = bd.projectC()
    bot.send_message(message.chat.id, "Название проекта")
    bot.register_next_step_handler(message,find_text)
    #bot.send_message(message.chat.id, "Введите категорию")
    #obj.category = find_text(bot)
    #bot.send_message(message.chat.id, "Описание проекта")
    #obj.description = find_text(bot)
    #bot.send_message(message.chat.id, "Процент реализации")
    #obj.percent_complete = find_text(bot)


def find_text(message, obj):


