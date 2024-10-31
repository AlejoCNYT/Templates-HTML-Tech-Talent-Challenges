cuentas = {"Andres": 100, "Camilo": 30, "Gabriel": 75, "Johan": 90}

dictionary = dict()
for clave in cuentas:
    if cuentas[clave] == 75:
        print("Encontrado")
    print(clave, cuentas[clave])
