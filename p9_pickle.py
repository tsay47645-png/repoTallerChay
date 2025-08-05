import pickle

# Diccionario de ejemplo
datos = {
    "nombre": "Luis",
    "edad": 25,
    "cursos": ["Python", "Matemáticas", "IA"]
}

# Guardar los datos en un archivo binario
with open("datos.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

print("Datos guardados correctamente.")


# Leer los datos desde el archivo
with open("datos.pkl", "rb") as archivo:
    datos_cargados = pickle.load(archivo)

print("Datos cargados:")
print(datos_cargados)