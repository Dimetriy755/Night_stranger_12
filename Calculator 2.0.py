while 1==1:
    while 1==1:
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
            print(" Incorrect entry, try entering the first number again!")
        else: 
            continue
            
    print("")   
    operation = str(input(" Enter operation: "))

    while 1==1:
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
            print(" Incorrect entry, try entering the second number again!")
        else: 
            continue
  
    if operation == ('+'):
        result = X + Y
        print(" Operation - [+] \n Result is: ", result)
    elif operation == ('-'):
        result = X - Y
        print(" Operation - [-] \n Result is: ", result)
    elif operation == ('*'):
        result = X * Y
        print(" Operation - [*] \n Result is: ", result)
    elif operation == ('**'):
        result = X ** Y
        print(" Operation - [**] \n Result is: ", result)
    elif operation == ('/'):
        if Y != 0:
            result = X / Y
            print(" Operation - [/] \n Result is: ", result)
        else:
            print("") 
            print(" Division by zero is impossible!")
    elif operation == ('//'):
        if Y != 0:
            result = X // Y
            print(" Operation - [//] \n Result is: ", result)
        else:
            print("") 
            print(" Division by zero is impossible!")
    elif operation == ('%'):
        if Y != 0:
            result = X % Y
            print(" Operation - [%] \n Result is: ", result)
        else:
            print("") 
            print(" Division by zero is impossible!")
    else:
        print("")   
        print(" Operation not recognized, repeat all over again!")
        
        
        
    
