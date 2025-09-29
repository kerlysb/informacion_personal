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
# 3. Verificar si existe la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 989 637829"
    print("Se agregó el teléfono al diccionario")
else:
    print("El teléfono ya existe en el diccionario")
print()
# 4. Eliminar la clave "edad"
del informacion_personal["edad"]
print("Se eliminó la clave 'edad' del diccionario")
print()
