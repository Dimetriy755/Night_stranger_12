import os

# used to clean the screen
os.system('cls' if os.name == 'nt' else 'clear')

while 1 == 1:
    print("")
    print(" A math expression is something like: 1+(35+5)-(7*8)/9 (without whitespaces)")
    try:
        print("")
        math_expression = input(" Enter a math expression: ")
        while (math_expression == (math_expression).replace(" ","")):
            break
        else:
            print("")
            print(" You entered a string characters or whitespaces, but you need numeric!")
            continue
        math_expression = (math_expression).replace(" ","")
        result = round(eval(math_expression),7) 
        print(type(result)) # find out the data type
        print("")
        print(" Result of %s is %s" % (math_expression, result))
        print(" --------------------------------------------------")
        C = str(input(" Please enter 'CLS' to clear the screen: "))
        C = os.system('cls')
        continue
    except (NameError, TypeError, ValueError, SyntaxError):
        print("")
        print(" You entered a string characters or whitespaces, but you need numeric!")
        continue
    except ZeroDivisionError:
        print("")
        print(" Division by zero is IMPOSSIBLE!!!")
        continue

    
    
    