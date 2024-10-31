estudiantes = {
    "Andres": 85,
    "Camilo": 70,
    "Elkin": 90,
    "Gabriel": 70,
    "Johan": 87,
    "Luis": 97,
    "Natalia": 90,
    "Orlando": 80,
    "Wendy": 89
}

suma_total = 0

for clave in estudiantes:
    suma_total += estudiantes[clave]

promedio = suma_total / len(estudiantes)

print(promedio)

calificacoes = estudiantes.values()
print(sum(calificacoes)/len(estudiantes))
