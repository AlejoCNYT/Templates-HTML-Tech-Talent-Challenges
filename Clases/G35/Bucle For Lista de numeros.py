numeros = [10, 15, 20, 25, 30, 35, 40, 45]

lista_par = []
lista_impar = []

for numero in numeros:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print("Lista de pares: " + str(lista_par) + " Lista de impares: " + str(lista_impar))