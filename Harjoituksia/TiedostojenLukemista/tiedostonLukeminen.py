f = open("TiedostojenLukemista/data.txt", "r")
numero = 1
for x in f:
    print(f"{numero}. {x}")
    numero += 1

try:
    f = open("TiedostojenLukemista/data2.txt", "r")
    print(f.read())

except:
    print("Tiedostoa ei löydy!")