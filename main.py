import telebot
import weather

bot = telebot.TeleBot("760842492:AAHLvYk97oXR1SQpOnVy4InLZ9b69qyUrto")

#Chat = 414407353

upd = bot.get_updates()
print(upd)

last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

print(bot.get_me())

def log(message,answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "Мои возможности ограничены. Sorry!"
    log(message, answer)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['start'])
def handle_text(message):
    answer = "Ну что же , начнем. Инвадур , ты ли это ?"
    log(message, answer)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['settings'])
def handle_text(message):
    answer = "Тут пусто)"
    log(message, answer)
    bot.send_message(message.chat.id,answer )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = weather.weather + ("\n") + str(weather.temperature)
    if message.text == "Олды на месте":
        answer = "Ряльно на месте. Дальше разговаривать не умею => олды всегда на месте"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Тоже":
        answer = "Вот и прекрасно"
        log(message, answer)
        bot.send_message(message.chat.id,answer)
    else:
        log(message, answer)
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True, interval=0)