
while 1==1:
    print("")
    string = str(input(" Enter your string: "))
    print(" -----------------------------------------------")
    string = string.replace(" ", "").lower() # убираем пробелы и переводим все символы в нижний регистр (для предложений)

    string_conversely = string[::-1] # переворачивание строки шиворот-навыворот {•_-}

    for i in string_conversely:                        
        if string == string_conversely:
            print("")
            print(" This is a palindrome ->", string)
            print(" -----------------------------------------------")
            break
        elif string != string_conversely:
            print("")
            print(" This is not a palindrome ->", string_conversely) 
            print(" -----------------------------------------------")
            break



