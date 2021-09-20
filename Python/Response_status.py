import requests

while 1 == 1:

        print("")
        print(" ------ MENU ------")
        print("")
        print(" 1 - new request \n 2 - exit")

        while 1 == 1:
            try:
                print("")
                P = input(" Enter the number of your choice: ")
                P = int(P)
                break
            except ValueError:
                print("")
                print(" Incorrect entry, try entering the number of your choice again!")
                continue

        if P == 1:

            while 1 == 1:
                try:
                    print("")
                    url = str(input(" Enter request URL: "))
                    response = requests.get(url)
                    break
                except BaseException:
                    print("")
                    print(" Invalid URL, try entering URL again!")
                    continue

            if response.status_code == 200:
                print("")
                print(" Status Code: 200 Success!")
            elif response.status_code == 404:
                print("")
                print(" Status Code: 404 Not Found.")
            else:
                print(" _______")

        elif P == 2:
            break
        else:
            break