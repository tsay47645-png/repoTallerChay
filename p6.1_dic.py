'''
Escribe un programa en Python que solicite al usuario el nombre y la edad de 5 personas. Luego debe:
Mostrar todos los nombres y sus edades.
Mostrar cuántas personas hay en total.
Buscar un nombre ingresado por el usuario y mostrar su edad (si existe).
Mostrar los nombres en orden alfabético.
'''

# Crear un diccionario vacío
personas = {}

# Solicitar datos de 5 personas
print("Ingresa nombre y edad de 5 personas:")
for i in range(5):
    nombre = input(f"Nombre {i + 1}: ")
    edad = int(input(f"Edad de {nombre}: "))
    personas[nombre] = edad  # Agregar al diccionario

# 1. Mostrar todos los nombres y edades
print("\nLista de personas y sus edades:")
for nombre, edad in personas.items():
    print(f"{nombre} → {edad} años")

# 2. Cantidad total de personas
print(f"\nTotal de personas: {len(personas)}")

# 3. Buscar un nombre
buscar = input("\nEscribe un nombre para buscar su edad: ")
if buscar in personas:
    print(f"{buscar} tiene {personas[buscar]} años.")
else:
    print(f"{buscar} no está en la lista.")

# 4. Mostrar los nombres en orden alfabético
print("\nNombres en orden alfabético:")
for nombre in sorted(personas.keys()):
    print(nombre)
