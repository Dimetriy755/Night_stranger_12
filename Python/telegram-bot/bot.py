import time
import random
import telebot
from pyowm import OWM
from telebot import types

# bot token from @BotFather 
token = '5289885170:AAGeVdIBnxB_2pNLBwh9kgcw5Ap3mLuxmRM'
bot = telebot.TeleBot(token)
answer = ['Да я такой! Мляк-мляк... 😋','Да-да-да, хвалите меня... 😝','А скоро я буду ещё круче! 🤩','Мне просто НЕТ равных! 😎','СПАСИБО я счастлив! 😅','ДА я вообще ОГОНЬ! 🔥']

# API KEY for pyowm 
owm = OWM('b75c1a1b026adea85db316994ee67a30')
mgr = owm.weather_manager()
city = None

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Назови число дня.")
    item2 = types.KeyboardButton("😀 Хей бот ты живой?!")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 
    "Радушно приветствую вас {0.first_name}!\nМоё имя <b>{1.first_name}</b> и я бот, будем знакомы.\nИспользуйте кнопки для взаимодействия.".
    format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, 
    'У меня имеется возможность сообщить вам супер точную информацию о погоде в вашем городе. Такого вам не сообщит даже Google!', 
    parse_mode='html', reply_markup=markup)

    time.sleep(4)
    # inline buttons
    markup = types.InlineKeyboardMarkup(row_width=3)
    Button1 = types.InlineKeyboardButton("Балахна", callback_data='1')
    Button2 = types.InlineKeyboardButton("Домодедово", callback_data='2')
    Button3 = types.InlineKeyboardButton("Калуга", callback_data='3')
    Button4 = types.InlineKeyboardButton("Кишинёв", callback_data='4')
    Button5 = types.InlineKeyboardButton("Красногорск", callback_data='5')
    Button6 = types.InlineKeyboardButton("Курск", callback_data='6')
    Button7 = types.InlineKeyboardButton("Москва", callback_data='7')
    Button8 = types.InlineKeyboardButton("Оренбург", callback_data='8')
    Button9 = types.InlineKeyboardButton("Воронеж", callback_data='9')
    markup.add(Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9)
    bot.send_message(message.chat.id, 
    'Я беру все свои данные о погоде из сверхсекретной метеорологической станции. Выберите свой город из списка и нажмите на его кнопку, чтобы узнать какая там сейчас погода.', 
    reply_markup=markup)

@bot.message_handler(content_types=['text'])
def talk(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Назови число дня.':
            bot.send_message(message.chat.id, str(random.randint(1,9)))
        elif message.text == '😀 Хей бот ты живой?!':
            bot.send_message(message.chat.id, 'Да я живее всех живых!!! 😜')
        elif message.text == "Круто" or message.text == "Вау" or message.text == "Круто!" or message.text == "Вау!" or message.text == "Вау! Круто!" or message.text == "Ты крутой!" or message.text == "Ты крутой" or message.text == "Вот это да!" or message.text == 'супер':
                bot.send_message(message.chat.id, random.choice(answer))
        elif message.text == 'Ты бот?' or message.text == "ты бот?" or message.text == 'Ты кто?' or message.text == "ты кто?" or message.text == 'Ты кто такой?' or message.text == 'Кто ты такой?' or message.text == "Кто ты?" or message.text == 'кто ты?':
            bot.send_message(message.chat.id, 'Я бот. Demetrios мой создатель. 🤷‍♂️')
        elif message.text == 'Что ты умеешь?' or message.text == "Что ты умеешь делать?" or message.text == 'Что ты можешь?':
                bot.send_message(message.chat.id, 'Я умею показывать ваше число дня. Самое первое число которое я вам покажу и будет вашим чилом дня.')
        elif message.text == 'бот' or message.text == "бот?" or message.text == 'Бот' or message.text == "Бот?":
            bot.send_message(message.chat.id, 'Что такое? Готов быть вам чем-то полезным. 😉')        
        else:
            # bot.send_message(message.chat.id, 'Я не знаю что вам ответить. 😢')
            bot.send_message(message.chat.id, 'Издеваетесь надо мной да?!')
            time.sleep(3)
            bot.send_message(message.chat.id, 'Ok! Тогда я всё-всё за вами буду повторять! 😝')
            time.sleep(3)
            bot.send_message(message.chat.id, 'Вот всё то, что вы мне писали:')
            bot.send_message(message.chat.id, message.text)
            bot.send_message(message.chat.id, message.text)
            bot.send_message(message.chat.id, message.text)
            time.sleep(2)
            bot.send_message(message.chat.id, '👹 хи-хи-хи...')
            time.sleep(2)
            # inline buttons
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да, я боюсь.", callback_data='Ok')
            item2 = types.InlineKeyboardButton("Не делай так.", callback_data='No')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'У меня больше! Страшно?!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Ok':
                bot.send_message(call.message.chat.id, 'Вот так то! Бойтесь меня! 😈')
            elif call.data == 'No':
                bot.send_message(call.message.chat.id, 'Ну я то злобненький! И конечно я буду так делать! 👹')
            elif call.data == '1':
                city = 'Балахна'
            elif call.data == '2':
                city = 'Домодедово'
            elif call.data == '3':
                city = 'Калуга'
            elif call.data == '4':
                city = 'Кишинёв'
            elif call.data == '5':
                city = 'Красногорск'
            elif call.data == '6':
                city = 'Курск'
            elif call.data == '7':
                city = 'Москва'
            elif call.data == '8':
                city = 'Оренбург'
            elif call.data == '9':
                city = 'Воронеж'

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="У меня больше! Страшно?!",
            reply_markup=None)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Я беру все свои данные о погоде из сверхсекретной метеорологической станции. Выберите свой город из списка и нажмите на его кнопку, чтобы узнать какая там сейчас погода.",
            reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ваш ответ был отправлен.")

        observation = mgr.weather_at_place(city)
        w = observation.weather

        # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0} - данные передаются в словаре
        # - это словарь Python (массив данных, где передаются пары - ключ: 'значение')
        # - и далее будет показано как вытащить нужное нам значение из словаря Python
        # temperature1 = w.temperature('celsius')['temp_max']
        temperature2 = w.temperature('celsius')['temp']
        # temperature3 = w.temperature('celsius')['temp_min']
        wind = w.wind()['speed'] # {'speed': 4.6, 'deg': 330}
        humidity = w.humidity # 87% (as a percentage)
        clouds = w.clouds # 75% (as a percentage)
        detailed_status = w.detailed_status # 'clouds'
        hPa = w.pressure['press']
        mmHg = hPa * 0.75006375541921
        mmHg = round(mmHg, 1)

        if detailed_status == 'overcast clouds':
            detailed_status = 'сплошная облачность'
        elif detailed_status == 'broken clouds':
            detailed_status = 'рассеянная облачность'
        elif detailed_status == 'clear sky':
            detailed_status = 'чистое небо'
        elif detailed_status == 'few clouds':
            detailed_status = 'имеется несколько облаков' 
        elif detailed_status == 'light intensity shower rain': 
            detailed_status = 'небольшой ливень'
        elif detailed_status == 'dust':
            detailed_status = 'весьма пыльно'
        elif detailed_status == 'scattered clouds':
            detailed_status = 'имеются разбросанные облака'
        elif detailed_status == 'shower rain':
            detailed_status = 'ливень'
        elif detailed_status == 'mist':
            detailed_status = 'туман'
        elif detailed_status == 'light rain':
            detailed_status = 'небольшой дождь'
        elif detailed_status == 'light snow':
            detailed_status = 'небольшой снег'

        # bot.send_message(call.from_user.id, "В городе " + city + " сейчас максимальная температура: " + str(temperature1) + "С°")
        bot.send_message(call.from_user.id, "В городе " + city + " сейчас средняя температура: " + str(temperature2) + " С°")
        # bot.send_message(call.from_user.id, "В городе " + city + " сейчас минимальная температура: " + str(temperature3) + "С°")
        bot.send_message(call.from_user.id, "В городе " + city + " скорость ветра сейчас составляет: " + str(wind) + " м/с")
        bot.send_message(call.from_user.id, "В городе " + city + " влажность сейчас составляет: " + str(humidity) + "%")
        bot.send_message(call.from_user.id, "В городе " + city + " облачность сейчас составляет: " + str(clouds) + "%")
        bot.send_message(call.from_user.id, "В городе " + city + " сейчас: " + str(detailed_status))
        bot.send_message(call.from_user.id, "В городе " + city + " атмосферное давление сейчас составляет: " + str(mmHg) + " мм рт.ст.")

    except UnboundLocalError as e:
        pass
# RUN
bot.polling(non_stop=True)
 
  