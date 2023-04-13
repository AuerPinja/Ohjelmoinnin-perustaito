ika = int(input("Anna ikäsi: "))

if ika < 0 or ika > 150:
    print("Virheellinen ikä!")

elif ika < 6:
    print("Esikoululainen")
elif ika == 14:
    print("Haastava ikä")
elif ika == 16 or ika == 17 or ika == 18:
    print("Lähes aikuinen")
elif ika > 18 and ika < 30:
    print("Olet täysi-ikäinen, muttet vielä keski-iän kriisissä")
elif ika >= 30 and ika < 45:
    print("Olet keski-iässä")
elif ika > 45 and ika < 65:
    print("Vielä ehtii ennen eläkettä")
else:
    print("Olet eläkeläinen")
