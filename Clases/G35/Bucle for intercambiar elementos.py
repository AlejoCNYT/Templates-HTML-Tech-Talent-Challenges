numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in range(len(numeros)):
    if index == 0:
        primero = numeros[index]
    elif index == len(numeros) - 1:
        numeros[0] = numeros[index]
        numeros[index] = primero

print(numeros)

temp = numeros[0]
numeros[0] = numeros[len(numeros) - 1]
numeros[len(numeros) - 1] = temp
print(numeros)
