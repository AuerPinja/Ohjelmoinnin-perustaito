nimi = input("Anna nimi: ")
f = open("TiedostojenLukemista/nimidata.txt", "r")
laskuri = 0
#print(f.read())

for i in f:
    laskuri += 1
    if i.find(nimi) >= 0:
        print(f"Nimi löytyi tiedoston {laskuri} riviltä!")
        break
    else:
        print("Nimeä ei löytnyt!")