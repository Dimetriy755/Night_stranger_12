from email_validator import validate_email, EmailNotValidError

# Задание 12.6.6. Написать программу для валидации вводимой почты установил модуль 
# «email_validator» (ver. 1.1.1) (через CMD => pip install email_validator)

while 1==1:
    print("")
    email = input(" Enter your email: ")
    print(" -----------------------------------------------")

    try:
    # Validate
        valid = validate_email(email)

    # Update with the normalized form
        email = valid.email
    except EmailNotValidError as e:
    # email is not valid, exception message is human readable
        print(str(e))