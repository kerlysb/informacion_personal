 1. Crear el diccionario con información personal
informacion_personal = {
    "nombre": "Kerly Suárez",
    "edad": 32,
    "ciudad": "Guayaquil",
    "profesion": "Estudiante de TIC"
}

print("Diccionario inicial:")
print(informacion_personal)
print()
# 2. Acceder y modificar el valor de "ciudad"
print("Ciudad original:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Quito"
print("Ciudad modificada:", informacion_personal["ciudad"])
print()

# Nota: La clave "profesion" ya existe desde el inicio
# Si no existiera, la agregaríamos así:
# informacion_personal["profesion"] = "Estudiante de TIC"
