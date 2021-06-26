while 1==1:
    print("")
    X = float(input(" Enter first number: "))
    print("")
    operation = str(input(" Enter operation: "))
    print("")
    Y = float(input(" Enter second number: "))
    print("")

    if operation == ('+'):
        result = X + Y
        print(" Operation - [+] \n Result is: ", result)
    elif operation == ('-'):
        result = X - Y
        print(" Operation - [-] \n Result is: ", result)
    elif operation == ('*'):
        result = X * Y
        print(" Operation - [*] \n Result is: ", result)
    elif operation == ('/'):
        if Y != 0:
            result = X / Y
            print(" Operation - [/] \n Result is: ", result)
        else:
            print(" Division by zero is impossible!")
    elif operation == ('//'):
        if Y != 0:
            result = X // Y
            print(" Operation - [//] \n Result is: ", result)
        else:
            print(" Division by zero is impossible!")
    elif operation == ('%'):
        if Y != 0:
            result = X % Y
            print(" Operation - [%] \n Result is: ", result)
        else:
            print(" Division by zero is impossible!")
    elif operation == ('**'):
        result = X ** Y
        print(" Operation - [**] \n Result is: ", result)
    else:
        print(" Operation not recognized!")
        
        
        
    
