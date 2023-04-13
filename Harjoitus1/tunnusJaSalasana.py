tunnus = input("Anna tunnus: ")
salasana = input("Anna salasana: ")

while tunnus != "Pinja" and salasana != "kissa123":
    print("Väärä tunnus ja salasana!")
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana: ")
else:
    print("Kirjautuminen onnistui!")