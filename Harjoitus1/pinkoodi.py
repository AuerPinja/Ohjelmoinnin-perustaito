pin = int(input("Anna PIN-koodi: "))

while pin != 3120:
    print("Väärä koodi!")
    pin = int(input("Anna PIN-koodi: "))
else: 
    print("Oikea koodi!")