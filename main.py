import telebot

import weather

import nbrb

import news

import sqlite3

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


def bd_add_user(message):
    conn = sqlite3.connect('telegram-db.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES ({0}, '{1}', '{2}')".format(message.from_user.id,
                                                                    message.from_user.first_name,
                                                                    message.from_user.last_name))
    conn.commit()
    c.close()
    conn.close()


def bd_add_message(message):
    conn = sqlite3.connect('telegram-db.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (user_id, message) VALUES ({0}, '{1}')".format(message.from_user.id,
                                                                                   message.text))
    conn.commit()
    c.close()
    conn.close()


@bot.message_handler(commands=['start'])
def handle_text(message):
    global last_message
    last_message = 'start'
    answer = "Начало положено"
    log(message)
    bd_add_user(message)
    bd_add_message(message)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    global last_message
    last_message = 'help'
    answer = "Справочная система Telegram Bot'a NWER" + "\n" + \
             "\n" + "Команды:" + \
             "\n" + "/weather - показывает прогноз погоды в введенном городе" + \
             "\n" + "Для отмены действия /weather введите команду Stop" + \
             "\n" + "При попытке ввода несуществующего города - выводится соответствующее сообщения" + "\n" + \
             "\n" + "/nbrb - выводит курс валют USD, EUR, RUB по собранным данным c сайта Национального Банка РБ" + \
             "\n" + "Курс валют выводится на дату отправки сообщения" + "\n" + \
             "\n" + "/news - выводит ТОП 10 мировых новостей" + \
             "\n" + "Команда Rus - выводит русскоязычные новости" + \
             "\n" + "Команда Eng - выводит англоязычные новости" + \
             "\n" + "Для отмены действия /news введите команду Stop"
    log(message)
    bd_add_message(message)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['weather'])
def handle_text(message):
    global last_message
    last_message = 'weather'
    answer = "Введите город для прогноза погоды"
    log(message)
    bd_add_message(message)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['nbrb'])
def handle_text(message):
    global last_message
    last_message = 'nbrb'
    from datetime import date
    answer = "Курс валют на " + "\n" + str(date.today())
    bot.send_message(message.chat.id, answer)
    rate = str(nbrb.USD['Cur_Scale']) + ' ' + nbrb.USD['Cur_Abbreviation'] + ' = ' + str(
        nbrb.USD['Cur_OfficialRate']) + "\n" + \
           str(nbrb.EUR['Cur_Scale']) + ' ' + nbrb.EUR['Cur_Abbreviation'] + ' = ' + str(
        nbrb.EUR['Cur_OfficialRate']) + "\n" + \
           str(nbrb.RUB['Cur_Scale']) + ' ' + nbrb.RUB['Cur_Abbreviation'] + ' = ' + str(nbrb.RUB['Cur_OfficialRate'])
    log(message)
    bd_add_message(message)
    bot.send_message(message.chat.id, rate)
    last_message = ''


@bot.message_handler(commands=['news'])
def handle_text(message):
    global last_message
    last_message = 'news'
    from datetime import date
    answer = "Новости на " + "\n" + str(date.today()) + "\n" + 'Выберите регион для показа новостей'
    log(message)
    bd_add_message(message)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    global last_message
    if last_message == 'weather':
        allweather = weather.get_weather_for_specific_city(message.text)
        log(message)
        bd_add_message(message)
        if message.text == 'Stop':
            answer = 'Отмена команды weather'
            bot.send_message(message.chat.id, answer)
            last_message = ''
        else:
            answer = message.text + "\n" + str(allweather)
            bot.send_message(message.chat.id, answer)
            last_message = ''
    elif last_message == 'news':
        log(message)
        bd_add_message(message)
        if message.text == 'Eng':
            all_news = news.news_now_eng
            for news_now in all_news['articles']:
                top_news = str(news_now['title']) + "\n" + str(news_now['url'])
                bot.send_message(message.chat.id, top_news)
                last_message = ''
        elif message.text == 'Rus':
            all_news = news.news_now_ru
            for news_now in all_news['articles']:
                top_news = str(news_now['title']) + "\n" + str(news_now['url'])
                bot.send_message(message.chat.id, top_news)
                last_message = ''
        elif message.text == 'Stop':
            answer = 'Отмена команды news'
            bot.send_message(message.chat.id, answer)
            last_message = ''
        else:
            answer = "Такого не существует"
            bot.send_message(message.chat.id, answer)
            last_message = ''
    elif message.text == 'Олды тут?':
        answer = 'На месте !'
        log(message)
        bd_add_message(message)
        bot.send_message(message.chat.id, answer)
    else:
        answer = "Такого не существует"
        log(message)
        bd_add_message(message)
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)