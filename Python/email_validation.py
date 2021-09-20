from email_validator import validate_email, EmailNotValidError
import time
import os

# Задание 12.6.6. Написать программу для валидации вводимой почты установил модуль 
# «email_validator» (ver. 1.1.1) (через CMD => pip install email_validator)

correct = str("Everything is correct, should be here - [OK].")

while 1==1:
    print("")
    email = input("Enter your email: ")
    try:
    # Validate
        valid = validate_email(email)

    # Update with the normalized form
        email = valid.email
        if (email == valid.email):
            print("---------------------------------------------")
            print(correct)
            time.sleep(30)
            break
    except EmailNotValidError as e:
    # email is not valid, exception message is human readable
        print("----------------------------------------------------------------")
        print(str(e))
        C = str(input("Press the [Enter] key to clear the screen - [CLS]."))
        C = os.system('cls')
        continue