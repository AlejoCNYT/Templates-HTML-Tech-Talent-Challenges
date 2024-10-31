
estudiantes = {
    "Andres": [4, 4.7, 3.8, 2.9],
    "Camilo": [4.3, 4., 3.8, 3.9],
    "Elkin": [3, 4.7, 3.8, 3.9],
    "Gabriel": [5, 4, 3.8, 4],
    "Johan": [4, 4, 3, 5],
    "Luis": [5, 3, 3, 4],
    "Natalia": [4, 4.7, 3, 3.9],
    "Orlando": [4, 4, 3.8, 3.9],
    "Wendy": [4, 4.2, 3.9, 5]
}


for estudiante in estudiantes:
    suma_calificaciones = 0
    for calificacion in estudiantes[estudiante]:

        suma_calificaciones += (float(calificacion))
    print(estudiante, suma_calificaciones/4)

# Solución clase

for nombre, promedios in estudiantes.items():
    promedio = sum(promedios)/len(promedios)
    print(f"Nombre: {nombre}, Promedios: {promedio}")
