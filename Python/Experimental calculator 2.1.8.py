from colorama import Fore, Back, Style
from colorama import init
import math
import time
import os

# used to clean the screen
os.system('cls' if os.name == 'nt' else 'clear')

# use Colorama to make Termcolor work on Windows too
init (autoreset = True)

def Multiple_addition_calculator():
    while 1==1:
        try:
            print("")
            X = float(input(" Enter first number: "))
            print("")
            Y = float(input(" Enter second number: "))
            print("")
            print(Fore.MAGENTA + " Calculate? Yes/No -> y/n enter: ", end='') 
            calculation = input()
            if calculation == ('y'):
                result = X + Y
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation != ('y') and calculation != ('n'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation == ('y') and calculation == ('n'):
                break
        
            print("")
            Z = float(input(" Enter third number: "))
            print("")
            print(Fore.MAGENTA + " Calculate? Yes/No -> y/n enter: ", end='') 
            calculation_1 = input()
            if calculation_1 == ('y'):
                result = X + Y + Z
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation_1 != ('y') and calculation_1 != ('n'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation_1 == ('y') and calculation_1 == ('n'):
                break
            
            print("")
            T = float(input(" Enter fourth number: "))
            print("")
            print(Fore.MAGENTA + " Calculate? Yes/No -> y/n enter: ", end='') 
            calculation_2 = input()
            if calculation_2 == ('y'):
                result = X + Y + Z + T
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation_2 != ('y') and calculation_2 != ('n'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation_2 == ('y') and calculation_2 == ('n'):
                break

            print("")
            R = float(input(" Enter fifth number: "))
            print("")
            print(Fore.MAGENTA + " Calculate? Yes/No -> y/n enter: ", end='') 
            calculation_3 = input()
            if calculation_3 == ('y'):
                result = X + Y + Z + T + R
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation_3 != ('y') and calculation_3 != ('n'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation_3 == ('y') and calculation_3 == ('n'):
                break

            print("")
            D = float(input(" Enter sixth number: "))
            print("")
            print(Fore.MAGENTA + " Calculate? Yes/No -> y/n enter: ", end='') 
            calculation_4 = input()
            if calculation_4 == ('y'):
                result = X + Y + Z + T + R + D
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation_4 != ('y') and calculation_4 != ('n'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation_4 == ('y') and calculation_4 == ('n'):
                break

            print("")
            S = float(input(" Enter seventh number: "))
            print("")
            print(Fore.MAGENTA + " Calculate? Yes/No -> y/n enter: ", end='') 
            calculation_5 = input()
            if calculation_5 == ('y'):
                result = X + Y + Z + T + R + D + S
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation_5 != ('y') and calculation_5 != ('n'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation_5 == ('y') and calculation_5 == ('n'):
                break

            print("")
            P = float(input(" Enter eighth number: "))
            print("")
            print(Fore.MAGENTA + " Calculate? Yes/No -> y/n enter: ", end='') 
            calculation_6 = input()
            if calculation_6 == ('y'):
                result = X + Y + Z + T + R + D + S + P
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation_6 != ('y') and calculation_6 != ('n'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation_6 == ('y') and calculation_6 == ('n'):
                break

            print("")
            G = float(input(" Enter ninth number: "))
            print("")
            print(Fore.MAGENTA + " Calculate? Yes/No -> y/n enter: ", end='') 
            calculation_7 = input()
            if calculation_7 == ('y'):
                result = X + Y + Z + T + R + D + S + P + G
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation_7 != ('y') and calculation_7 != ('n'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation_7 == ('y') and calculation_7 == ('n'):
                break

            print("")
            J = float(input(" Enter tenth number: "))
            print("")
            print(Fore.MAGENTA + " Last number! You can enter ONLY Yes -> y enter: ", end='')
            calculation_8 = input()
            if calculation_8 == ('y'):
                result = X + Y + Z + T + R + D + S + P + G + J
                print("\n Result is:", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
                break
            elif calculation_8 != ('y'):
                print(Fore.RED + "\n Error. Unknown answer.")
                continue
            elif calculation_8 == ('y'):
                break
        except ValueError:
                print("")
                print(Fore.YELLOW + " You entered a string character, but you need numeric!")
                continue

while 1 == 1:

    print("")
    print(" ---------------------- MENU ----------------------")
    print("")
    print(" 0 - Multiple addition calculator [up to ten terms]")
    print(" 1 - Operation calculate the root of a number:[ √ ]")
    print(" 2 - Operation calculate: [ +, -, *, **, /, //, % ]\n 3 - Exit")
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
        Multiple_addition_calculator()

    elif P == 1:
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
            
    elif P == 2:

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
                print(" Operation - [+] \n \n Result is -", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
            elif operation == ('-'):
                result = X - Y
                print("")
                print(" Operation - [-] \n \n Result is -", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
            elif operation == ('*'):
                result = X * Y
                print("")
                print(" Operation - [*] \n \n Result is -", result)
                print(" --------------------------------------------------")
                C = str(input(" Please enter 'CLS' to clear the screen: "))
                C = os.system('cls')
            elif operation == ('**'):
                if X > 0 and Y >= 0.5 or X != X * (-1) and Y != 0.5:
                    result = X ** Y
                    print("")
                    print(" Operation - [**] \n \n Result is -", result)
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
                    print(" Operation - [/] \n \n Result is -", result)
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
                    print(" Operation - [//] \n \n Result is -", result)
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
                    print(" Operation - [%] \n \n Result is -", result)
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

    elif P == 3:
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