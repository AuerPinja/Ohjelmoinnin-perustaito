print("SYÖTÄ HENKILÖTIEDOT")
print("-------------------")
print("")
nimi = input("Anna etunimet: ")
sukunimi = input("Anna sukunimi: ")
puhelinnumero = input("Anna puhelinnumero: ")
sposti = input("Anna sähköposti: ")
osoite = input("Anna lähiosoite: ")
postinumero = input("Anna postinumero: ")
kaupunki = input("Anna kaupunki: ")
maa = input("Anna maa: ")
vuosi = int(input("Anna syntymävuosi: "))
print("")
print("KIITOS!")
print("")
print("")
print("HENKILÖN TIEDOT")
print("---------------")
print("")
print("NIMI:")
print(f"    {sukunimi}, {nimi}")
print("PUH:")
print(f"    {puhelinnumero}")
print("E-MAIL")
print(f"    {sposti}")
print("OSOITE:")
print(f"    {osoite}")
print(f"    {postinumero} {kaupunki}")
print(f"    {maa}")
print("IKÄ:")
print(f"    {2023 - vuosi}")