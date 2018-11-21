import telebot

import weather

import nbrb

bot = telebot.TeleBot("760842492:AAHLvYk97oXR1SQpOnVy4InLZ9b69qyUrto")

# Chat = 414407353

upd = bot.get_updates()
print(upd)

last_upd = upd[-1]
message_from_user = last_upd.message

last_message = ''

print(message_from_user)
print(bot.get_me())

def log(message):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))

@bot.message_handler(commands=['start'])
def handle_text(message):
    global last_message
    last_message = 'start'
    answer = "Начало положено"
    log(message)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    global last_message
    last_message = 'help'
    answer = "Справочная система"
    log(message)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['weather'])
def handle_text(message):
    global last_message
    last_message = 'weather'
    answer = "Введите город для прогноза погоды"
    log(message)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['nbrb'])
def handle_text(message):
    global last_message
    last_message = 'nbrb'
    answer = "Курс валют"
    log(message)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global last_message
    if last_message == 'weather':
        allweather = weather.get_weather_for_specific_city(message.text)
        log(message)
        if message.text == 'Stop':
            answer = 'Отмена команды weather'
            log(message)
            bot.send_message(message.chat.id, answer)
            last_message = ''
        else:
            answer = message.text + "\n" + str(allweather)
            bot.send_message(message.chat.id, answer)
            last_message = ''
    elif last_message == 'nbrb':
        UAH = (nbrb.UAH['Cur_OfficialRate'])
        EUR = (nbrb.EUR['Cur_OfficialRate'])
        log(message)
        bot.send_message(message.chat.id, UAH)
        bot.send_message(message.chat.id, EUR)
        last_message = ''
    else:
        answer = "Такого не существует"
        log(message)
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True, interval = 0)