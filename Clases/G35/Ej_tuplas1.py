tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)
tupla_multiplicada = tupla_concatenada * 3
print(tupla_multiplicada)

for elemento in tupla_concatenada:
    print(elemento * 3, end = " ")
print("\n")

numero = int(input("Ingrese el número: "))
for elemento in tupla_concatenada:
    print(elemento * numero, end = " ")
print("\n")

for index in range(len(tupla_concatenada) ):
    print(tupla_concatenada[len(tupla_concatenada) - 1 - index], end= " ")
