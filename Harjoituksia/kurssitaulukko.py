print("********************************")
print("*** Euroa      =       Markkaa *")
print("********************************")
print("")
kurssi = 5.94573
eurot = [1,2,3,4,5,6,7,8,9,10]

for x in eurot:
   markka = x * kurssi
   markka = str(round(markka, 2))
   print(f"\t     {x} = {markka}")
   
