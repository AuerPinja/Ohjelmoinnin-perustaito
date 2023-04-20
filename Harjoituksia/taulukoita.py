luvut = [5, 7, 32, 31, 8]
desimaalit = [12.4, -13.55, 67.44]
kaupungit = ["Helsinki", "Lissabon", "New York", "Shanghai"]

print(f"Alkiossa numero 3 on {kaupungit[3]}")
print(f"Alkiossa numero 5 on {luvut[4]}")
print(f"Desimaalitaulukossa on {len(desimaalit)} arvoa")

# Kirjoita kokonaislukutaulukkoa varten while-silmukka, jolla tulostat taulukon sisällön ruudulle alusta loppuun
i = 0

while i < len(luvut):
    print(luvut[i])
    i = i + 1

# Kirjoita desimaalilukutaulukkoa varten while–silmukka, jolla tulostat taulukon viimeisestä alkiosta ensimmäiseen (eli käänteisessä järjestyksessä). 
x = 0

while x < len(desimaalit):
    desimaalit.reverse()
    print(desimaalit[x])
    x = x + 1


for a in kaupungit:
    print(a, end = ", ")
