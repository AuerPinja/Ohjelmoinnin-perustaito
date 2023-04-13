vuodet = [*range(1753, 2050)]

for x in vuodet:
    if (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0):
        print(f"{x} on karkausvuosi")

# kesken