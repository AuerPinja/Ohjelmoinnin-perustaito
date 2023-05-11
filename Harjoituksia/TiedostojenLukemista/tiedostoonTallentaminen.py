try:
    f = open("TiedostojenLukemista/syotteet.txt", "x")

except:
    print("Tiedosto on luotu")

with open ("TiedostojenLukemista/syotteet.txt", "a") as syotteet:
    syote = input("Kirjoita jotain: ")
    syotteet.write(syote+"\n")