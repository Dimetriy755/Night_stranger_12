from colorama import Fore, Back, Style
from colorama import init
import math
import time
import os

# used to clean the screen
os.system('cls' if os.name == 'nt' else 'clear')

# use Colorama to make Termcolor work on Windows too
init (autoreset = True)

while 1 == 1:

    print("")
    print(" ---------------------- MENU ----------------------")
    print("")
    print("")
    print(" 0 - Operation calculate the root of a number:[ √ ]")
    print(" 1 - Operation calculate: [ +, -, *, **, /, //, % ]\n 2 - Exit")
    print(Fore.YELLOW + " Ignore CLS on screen cleaning, return to the menu!")
    print(" --------------------------------------------------")

    while 1 == 1:
        try:
            print("")
            P = input(" Enter the number of your choice: ")
            P = int(P)
            break
        except ValueError:
            print("")
            print(Fore.YELLOW + " Incorrect entry, try entering the number of your choice again.")
            continue

    if P == 0:
        while 1 == 1:
            try:
                print("")
                Z = input(" Enter a number to calculate its square root: ")
                Z = float(Z)
                N = math.sqrt(Z)
                N = float(N)
                print("")
                print(" The square root of", Z, "is", N)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            except ValueError:
                print("")
                print(Fore.YELLOW + " Wrong entry, try entering the number for square root again.")
                print(Fore.YELLOW + " You can not enter non-numeric symbols and negative numbers!")
                continue
            
    elif P == 1:

        while 1 == 1:
            try:
                print("")
                X = input(" Enter first number: ")
                X = float(X)
                if X == float:
                    break
                else:
                    break
            except ValueError:
                print("")
                print(Fore.YELLOW + " Incorrect entry, try entering the first number again.")
                continue

        print("")
        operation = str(input(" Enter operation: "))

        while 1 == 1:
            try:
                print("")
                Y = input(" Enter second number: ")
                Y = float(Y)
                if Y == float:
                    break
                else:
                    break
            except ValueError:
                print("")
                print(Fore.YELLOW + " Incorrect entry, try entering the second number again.")
                continue

        try:
            if operation == ('+'):
                result = X + Y
                print("")
                print(" Operation - [+] \n Result is -", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
            elif operation == ('-'):
                result = X - Y
                print("")
                print(" Operation - [-] \n Result is -", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
            elif operation == ('*'):
                result = X * Y
                print("")
                print(" Operation - [*] \n Result is -", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
            elif operation == ('**'):
                if X > 0 and Y >= 0.5 or X != X * (-1) and Y != 0.5:
                    result = X ** Y
                    print("")
                    print(" Operation - [**] \n Result is -", result)
                    print(" --------------------------------------------------")
                    C = str(input(" Please enter 'CLS' to clear the screen: "))
                    C = os.system('cls')
                else:
                    print("")
                    print(Fore.RED + " The operation (example:-X **(Y = 0.5)) of extracting")
                    print(Fore.RED + " a square root from a negative number is FORBIDDEN!!!")
                    print(" ----------------------------------------------------")
                    C = str(input(" Please enter 'CLS' to clear the screen: "))
                    C = os.system('cls')
            elif operation == ('/'):
                if Y != 0:
                    result = X / Y
                    print("")
                    print(" Operation - [/] \n Result is -", result)
                    print(" --------------------------------------------------")
                    C = str(input(" Please enter 'CLS' to clear the screen: "))
                    C = os.system('cls')
                else:
                    print("")
                    print(Fore.RED + " Division by zero is IMPOSSIBLE!!!")
                    print(" --------------------------------------------------")
                    C = str(input(" Please enter 'CLS' to clear the screen: "))
                    C = os.system('cls')
            elif operation == ('//'):
                if Y != 0:
                    result = X // Y
                    print("")
                    print(" Operation - [//] \n Result is -", result)
                    print(" --------------------------------------------------")
                    C = str(input(" Please enter 'CLS' to clear the screen: "))
                    C = os.system('cls')
                else:
                    print("")
                    print(Fore.RED + " Division by zero is IMPOSSIBLE!!!")
                    print(" --------------------------------------------------")
                    C = str(input(" Please enter 'CLS' to clear the screen: "))
                    C = os.system('cls')
            elif operation == ('%'):
                if Y != 0:
                    result = X % Y
                    print("")
                    print(" Operation - [%] \n Result is -", result)
                    print(" --------------------------------------------------")
                    C = str(input(" Please enter 'CLS' to clear the screen: "))
                    C = os.system('cls')
                else:
                    print("")
                    print(Fore.RED + " Division by zero is IMPOSSIBLE!!!")
                    print(" --------------------------------------------------")
                    C = str(input(" Please enter 'CLS' to clear the screen: "))
                    C = os.system('cls')
            else:
                print("")
                print(Fore.YELLOW + " Operation not recognized[?] please try all over again.")
                print(Fore.YELLOW + " Look in the menu above on instructions for operations.")
                print(" ------------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
        except OverflowError:
            print("")
            print(Fore.RED + " Your result is too HUGE this number is much higher than the last")
            print(Fore.RED + " number that has a name in science as quadragintillion (1E123)!!!")
            print(Fore.GREEN + " Python calculator is not ready for this, we apologize¯\_{•_•}_/¯")
            print(" ----------------------------------------------------------------")
            C = str(input(" Please enter 'CLS' to clear the screen: "))
            C = os.system('cls')
            continue

    elif P == 2:
        print("")
        print(Fore.GREEN + " Bye bye user!{•_-}\n See you soon baby!")
        print(" Program ended. Exit.")
        print(" --------------------------------------------------")
        break
    else:
        print("")
        print(Fore.YELLOW + " Wrong way, try entering the number again after looking at the instructions.")
        print(Fore.YELLOW + " Look in the menu above this message which of the numbers you need to enter.")
        print(" ---------------------------------------------------------------------------")
        C = str(input(" Please enter 'CLS' to clear the screen: "))
        C = os.system('cls')

time.sleep(4)