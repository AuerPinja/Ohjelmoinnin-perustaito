arvosanaindeksi = 0
arvosanalista = []

while arvosanaindeksi  < 5:
    arvosana = int(input("Anna arvosana: "))
    arvosanalista.append(arvosana)
    arvosanaindeksi  = arvosanaindeksi  + 1

print(sum(arvosanalista))
print(sum(arvosanalista)/len(arvosanalista))

