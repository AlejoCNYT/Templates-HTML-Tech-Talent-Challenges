numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# agregar un elemento a una lista
numeros.append(11)
abecedario.append('k')

print(numeros)
print(abecedario)

# Extend extiende los elementos de una lista
numeros.extend([12, 13])
abecedario.extend(['l','m'])

print(numeros)
print(abecedario)

# insert insertar un elemento 'x' en la posición i
numeros.insert(2, 'a')
abecedario.insert(2,10)
print(numeros)
print(abecedario)

# remove borra 1er elemento de una lista
numeros.remove('a')
print(numeros)
"""numeros.remove(0)
print(numeros)"""
abecedario.remove(10)
print(abecedario)

# pop elimina el eleento en el índice seleccionado
numeros.pop(0)
print(numeros)

# clear vacía la lista
numeros.clear()
print(numeros)

# index devuelve el ínice de un valor buscado en un arreglo
numeros = [1, 2, 3, 4, 2, 6, 4, 4, 8, 10, 25]
print(numeros)
n=numeros.index(25)
print(n)

# count contar el número de veces que un elemento está en la lista
numeros.count(1)
print(numeros.count(4))

# sort Ordena elementos de una lista, ascendentemente
numeros.sort()
print(numeros)

# reverse da el bote a una lista (orden descendente)
numeros.reverse()
print(numeros)

# copi copia elementos de una lista
copia = numeros.copy()
print(numeros)
print(copia)

print(len(numeros))
print(len(abecedario))
print(max(numeros))
print(min(numeros))
print(max(abecedario))
print(min(abecedario))

print(sum(numeros))
