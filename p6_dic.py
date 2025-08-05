persona = {"nombre": "Ana","edad": 30,"ciudad": "Monterrey"}

#Mostrar las llaves del diccionario
print("Llaves: ", persona.keys())

# Acceder a valores
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# Agregar un nuevo dato
persona["profesion"] = "Ingeniera"

# Modificar un valor
persona["edad"] = 31

# Eliminar un dato
del persona["ciudad"]

# Recorrer el diccionario
print("\nDatos actualizados:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
