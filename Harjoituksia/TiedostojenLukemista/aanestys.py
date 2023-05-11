count_a = 0
count_b = 0
count_c = 0
count_d = 0

data = open("TiedostojenLukemista/aanestysdata.csv", "r")

for i in data:
    if i.find("a") <= 0:
        count_a += 1
    elif i.find("b") <= 0:
        count_b += 1
    elif i.find("c") <= 0:
        count_c += 1
    elif i.find("d") <= 0:
        count_d += 1
    else:
        print("Error")

print(count_a)
print(count_b)
print(count_c)
print(count_d)