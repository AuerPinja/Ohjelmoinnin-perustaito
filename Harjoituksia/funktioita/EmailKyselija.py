def kysyEmail():
    while True:
        email = input("Anna sähköposti: ")
        lenght = len(email)
        if email.find("@") and lenght > 6:
            print("True")
            break
        else:
            print("False")

kysyEmail()
    
