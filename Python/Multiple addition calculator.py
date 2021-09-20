import time
import os

while 1==1:
    try:
        print("")
        X = float(input(" Enter first number: "))
        print("")
        Y = float(input(" Enter second number: "))
        print("")
        calculation = str(input(" Calculate? Yes/No -> y/n enter: "))
        if calculation == ('y'):
            result = X + Y
            print("\n Result is:", result)
            break
        elif calculation != ('y') and calculation != ('n'):
            print(" Error. Unknown answer.")
            continue
        elif calculation == ('y') and calculation == ('n'):
            break
    
        print("")
        Z = float(input(" Enter third number: "))
        print("")
        calculation_1 = str(input(" Calculate? Yes/No -> y/n enter: "))
        if calculation_1 == ('y'):
            result = X + Y + Z
            print("\n Result is:", result)
            break
        elif calculation_1 != ('y') and calculation_1 != ('n'):
            print(" Error. Unknown answer.")
            continue
        elif calculation_1 == ('y') and calculation_1 == ('n'):
            break
        
        print("")
        T = float(input(" Enter fourth number: "))
        print("")
        calculation_2 = str(input(" Calculate? Yes/No -> y/n enter: "))
        if calculation_2 == ('y'):
            result = X + Y + Z + T
            print("\n Result is:", result)
            break
        elif calculation_2 != ('y') and calculation_2 != ('n'):
            print(" Error. Unknown answer.")
            continue
        elif calculation_2 == ('y') and calculation_2 == ('n'):
            break

        print("")
        R = float(input(" Enter fifth number: "))
        print("")
        calculation_3 = str(input(" Calculate? Yes/No -> y/n enter: "))
        if calculation_3 == ('y'):
            result = X + Y + Z + T + R
            print("\n Result is:", result)
            break
        elif calculation_3 != ('y') and calculation_3 != ('n'):
            print(" Error. Unknown answer.")
            continue
        elif calculation_3 == ('y') and calculation_3 == ('n'):
            break

        print("")
        D = float(input(" Enter sixth number: "))
        print("")
        calculation_4 = str(input(" Calculate? Yes/No -> y/n enter: "))
        if calculation_4 == ('y'):
            result = X + Y + Z + T + R + D
            print("\n Result is:", result)
            break
        elif calculation_4 != ('y') and calculation_4 != ('n'):
            print(" Error. Unknown answer.")
            continue
        elif calculation_4 == ('y') and calculation_4 == ('n'):
            break

        print("")
        S = float(input(" Enter seventh number: "))
        print("")
        calculation_5 = str(input(" Calculate? Yes/No -> y/n enter: "))
        if calculation_5 == ('y'):
            result = X + Y + Z + T + R + D + S
            print("\n Result is:", result)
            break
        elif calculation_5 != ('y') and calculation_5 != ('n'):
            print(" Error. Unknown answer.")
            continue
        elif calculation_5 == ('y') and calculation_5 == ('n'):
            break

        print("")
        P = float(input(" Enter eighth number: "))
        print("")
        calculation_6 = str(input(" Calculate? Yes/No -> y/n enter: "))
        if calculation_6 == ('y'):
            result = X + Y + Z + T + R + D + S + P
            print("\n Result is:", result)
            break
        elif calculation_6 != ('y') and calculation_6 != ('n'):
            print(" Error. Unknown answer.")
            continue
        elif calculation_6 == ('y') and calculation_6 == ('n'):
            break

        print("")
        G = float(input(" Enter ninth number: "))
        print("")
        calculation_7 = str(input(" Calculate? Yes/No -> y/n enter: "))
        if calculation_7 == ('y'):
            result = X + Y + Z + T + R + D + S + P + G
            print("\n Result is:", result)
            break
        elif calculation_7 != ('y') and calculation_7 != ('n'):
            print(" Error. Unknown answer.")
            continue
        elif calculation_7 == ('y') and calculation_7 == ('n'):
            break

        print("")
        J = float(input(" Enter tenth number: "))
        print("")
        calculation_8 = str(input(" Last number! You can enter ONLY Yes -> y enter: "))
        if calculation_8 == ('y'):
            result = X + Y + Z + T + R + D + S + P + G + J
            print("\n Result is:", result)
            break
        elif calculation_8 != ('y'):
            print(" Error. Unknown answer.")
            continue
        elif calculation_8 == ('y'):
            break
    except ValueError:
            print("")
            print(" You entered a string character, but you need numeric!")
            continue
        
time.sleep(12)
    

    