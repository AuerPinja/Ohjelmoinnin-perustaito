vuodet = [1753 - 2050]

for x in vuodet:
    x = x // 400
    if x == 0:
        print(f"Vuosi {x} oli karkausvuosi")

# kesken