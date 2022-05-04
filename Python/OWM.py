import time
from pyowm import OWM

while 1 == 1:
    try:
        print("")
        city = str(input('Впишите название своего города, чтобы\nузнать какая там сейчас погода: '))

        # API KEY
        owm = OWM('b75c1a1b026adea85db316994ee67a30')
        mgr = owm.weather_manager()

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

        print("")
        # print("В городе " + city + " сейчас максимальная температура: " + str(temperature1) + "С°")
        print("В городе " + city + " сейчас средняя температура: " + str(temperature2) + " С°")
        # print("В городе " + city + " сейчас минимальная температура: " + str(temperature3) + "С°")
        print("")
        print("В городе " + city + " скорость ветра сейчас составляет: " + str(wind) + " м/с")
        print("")
        print("В городе " + city + " влажность сейчас составляет: " + str(humidity) + "%")
        print("")
        print("В городе " + city + " облачность сейчас составляет: " + str(clouds) + "%")
        print("")
        print("В городе " + city + " сейчас: " + str(detailed_status))
        print("")
        print("В городе " + city + " атмосферное давление сейчас составляет: " + str(mmHg) + " мм рт.ст.")

    except BaseException as e:
        pass
        continue
    
    time.sleep(20)
    break


