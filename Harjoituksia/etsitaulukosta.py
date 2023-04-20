lukuTaulu = [55, 23, 6456, 324, 21, 234 , 72, 21]
nimiTaulu = ["Petteri", "Kauko", "Matti", "Minna", "Maisa", "Juuso", "Mauno"]

# 	Tee ohjelma, joka käy lukutaulun läpi ja etsii sieltä lukua 324. Kun luku löytyy, ohjelma tulostaa sen ruudulle. 
for i in lukuTaulu:
    if i == 324:
        print("Tästä listasta löytyi luku 324")

#   Tee ohjelma, joka kysyy käyttäjältä: ”Ketä haluat etsiä? ”. Lue käyttäjän antama vastaus talteen ja etsi löytyykö kyseinen nimi nimiTaulu-taulukosta. Jos nimi löytyy, tulostetaan mistä alkiosta se löytyy. Jos sitä ei löydy, tulostetaan ”Nimeä ei löytynyt”.
#   Tee kyselystä sinnikäs while-silmukan avulla. Eli kyselyä toistetaan niin kauan kunnes käyttäjä syöttää komennon 

henkilo = input("Ketä haluat etsiä? ")
x = 0

while x < len(nimiTaulu):
    if henkilo == "Lopeta":
        print("Kiitos!")
        break
    if henkilo in nimiTaulu:
        print(f"Henkilö {henkilo} löytyi listasta")
        henkilo = input("Ketä haluat etsiä? ")
    else:
        print(f"Henkilöä {henkilo} ei löytynyt listasta")
        henkilo = input("Ketä haluat etsiä? ")