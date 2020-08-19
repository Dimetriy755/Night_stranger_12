import math
import time

while 1 == 1:

    print("")
    print(" ---------------------- MENU ----------------------")
    print("")
    print("")
    print(" 0 - Operation calculate the root of a number [ √ ]")
    print(" 1 - Operation calculate:[ +, -, *, **, /, //, %, ]\n 2 - Exit")

    while 1 == 1:
        try:
            print("")
            P = input(" Enter the number of your choice: ")
            P = int(P)
            break
        except ValueError:
            print("")
            print(" Incorrect entry, try entering the number of your choice again.")
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
                break
            except ValueError:
                print("")
                print(" Wrong entry, try entering the number for square root again.")
                print(" You can not enter non-numeric symbols and negative numbers!")
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
                print(" Incorrect entry, try entering the first number again.")
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
                print(" Incorrect entry, try entering the second number again.")
                continue

        try:
            if operation == ('+'):
                result = X + Y
                print("")
                print(" Operation - [+] \n Result is -", result)
            elif operation == ('-'):
                result = X - Y
                print("")
                print(" Operation - [-] \n Result is -", result)
            elif operation == ('*'):
                result = X * Y
                print("")
                print(" Operation - [*] \n Result is -", result)
            elif operation == ('**'):
                result = X ** Y
                print("")
                print(" Operation - [**] \n Result is -", result)
            elif operation == ('/'):
                if Y != 0:
                    result = X / Y
                    print("")
                    print(" Operation - [/] \n Result is -", result)
                else:
                    print("")
                    print(" Division by zero is impossible!")
            elif operation == ('//'):
                if Y != 0:
                    result = X // Y
                    print("")
                    print(" Operation - [//] \n Result is -", result)
                else:
                    print("")
                    print(" Division by zero is impossible!")
            elif operation == ('%'):
                if Y != 0:
                    result = X % Y
                    print("")
                    print(" Operation - [%] \n Result is -", result)
                else:
                    print("")
                    print(" Division by zero is impossible!")
            else:
                print("")
                print(" Operation not recognized[?] please try all over again.")
                print(" Look in the menu below on instructions for operations.")
        except OverflowError:
            print("")
            print(" Your result is too HUGE this number is much higher than the last")
            print(" number that has a name in science as quadragintillion (1E123)!!!")
            print(" Python calculator is not ready for this, we apologize¯\_{•_•}_/¯")
            continue

    elif P == 2:
        print("")
        print(" Program ended. Exit. Bye bye user! See you soon babe! {•_-}")
        break
    else:
        print("")
        print(" Wrong way, try entering the number again after looking at the instructions.")
        print(" Look in the menu under this message which of the numbers you need to enter.")

time.sleep(4)
