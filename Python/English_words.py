from colorama import Fore
from colorama import init
import random
import time
import os

# used to clean the screen
os.system('cls' if os.name == 'nt' else 'clear')

# use Colorama to make Termcolor work on Windows too
init (autoreset = True)

print("")
print(Fore.YELLOW + " Просто пропускайте слова по клавише «Enter»,\n на которые вы уже 100% ответили правильно \n и очищайте экран консоли —> «CLS».")

while 1 == 1:

    a = ["True", "False", "Fly", "Crawl", "Lick", "Compress", "Meets", "Distinct", "Software",
    "Prey", "Sacrifice", "Response", "Request", "Result", "Human", "Flower", "Like", "Exception", 
    "Present", "Yesterday", "Beyond", "Catch", "Requirements", "Case", "Log", "Alike", "Access", "Denied", 
    "Expected", "Actual", "Quality", "Assurance", "User", "Experience", "Interface", "Row", "Amount", "Quantity"]
    print("")
    print(" Выбор слова случайный:", random.choice(a))

    print("")
    с = str(input(" Введите это слово на английском языке: "))
    print("")
       
    if с == ("Fly "):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Летать "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Crawl"):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Ползать"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("False"):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Ложь"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("True "):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Истина"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Lick"):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Лизать"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Compress"):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Сжимать"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Meets"):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Знакомиться"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Human "):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Человек "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Flower "):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Цветок "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Present"):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Подарок"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Yesterday"):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Вчера "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Beyond"):
        b = str(input(" Ведите перевод слова на русском языке: "))
        if b == ("Вне "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue     
    elif с == ("Catch "):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Ловить"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Prey"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Добыча"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Sacrifice"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Жертвоприношение"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Requirements "):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Требования"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Case"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Случай"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Log"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Журнал"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Response"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Ответ "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Request"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Запрос"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Expected"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Ожидаемый"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Actual "):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Фактический "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Result"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Результат "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Quality"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Качество "):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Assurance "):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Гарантия"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("User"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Пользователь"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("User"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Пользователь"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Experience"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Опыт"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Interface"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Интерфейс"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Like"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Наподобие"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Row"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Ряд"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Alike"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Одинаково"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Distinct"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Отчетливо"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Amount"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Сумма"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Quantity"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Количество"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Access"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Доступ"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Denied"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Отклонен"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Exception"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Исключение"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    elif с == ("Software"):
        d = str(input(" Ведите перевод слова на русском языке: "))
        if d == ("Программное обеспечение"):
            print("")
            print(Fore.GREEN + " Правильно!")
            print(" ==========================")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
        else:
            print("")
            print(Fore.RED + " Ошибка!")
            print(" --------------------------")
            C = str(input(" Нажать —> «Enter» —> «CLS»"))
            C = os.system('cls')
            continue
    else:
        print("")
        print(Fore.RED + " Ошибка!")
        print(" --------------------------")
        C = str(input(" Нажать —> «Enter» —> «CLS»"))
        C = os.system('cls')
        continue


time.sleep(8)