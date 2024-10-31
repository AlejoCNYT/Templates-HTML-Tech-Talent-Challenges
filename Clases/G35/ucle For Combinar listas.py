lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

lista3 = []

for index in range(len(lista1)):
    lista3.append(lista2[index])
    lista2[index] = lista1[index]
    lista1[index] = lista3[index]

print("l2: " + str(lista2) + " l1: " + str(lista1))
