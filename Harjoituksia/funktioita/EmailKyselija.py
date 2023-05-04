def kysyEmail():
    email = input("Anna sähköposti: ")
    at = email.find("@")
    if at == "@" and email > len(6):
        print("True")
    else:
        print("False")

kysyEmail()
    
