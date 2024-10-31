"""Contar la frecuencia de palabras"""

texto = "hola mundo hola python hola mundo hola"
texto_palabras = texto.split(" ")

frecuencia_palabras = {}

for clave in texto_palabras:
    frecuencia_palabras[clave] = texto_palabras.count(clave)

print(frecuencia_palabras)
