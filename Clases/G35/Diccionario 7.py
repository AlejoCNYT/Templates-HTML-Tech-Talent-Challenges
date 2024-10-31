diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(diccionario)
diccionario.clear()
print(diccionario)

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(diccionario)
diccionario_copia = diccionario.copy()
print(diccionario_copia)

print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())

diccionario.pop('f')
print(diccionario)

print(diccionario.pop('f', 0))

valor = diccionario.popitem()
print(valor)
print(diccionario)

diccionario2 = {"z": 20, "y": 19}
diccionario.update(diccionario2)
print(diccionario)
