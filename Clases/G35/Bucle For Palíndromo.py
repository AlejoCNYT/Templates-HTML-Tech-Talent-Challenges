from operator import index

palabra = list(input("Ingrese la palabra: ").replace(" ", ""))
print(palabra)
tamano = len(palabra)

for index in range(tamano // 2):
    if str(palabra[index]) == str(palabra[tamano - 1 - index]):
        # print(str(palabra[index]) + " " + str(palabra[tamano - 1 - index]))
        res = "Palabra palíndroma."
        continue
    else:
        res = "No es palíndroma"
        break

print(res)
