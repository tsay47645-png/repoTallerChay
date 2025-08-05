''' 
Escribe un programa en Python que solicite al usuario una lista de 5 nombres de personas. Luego, el programa debe:
Mostrar la lista completa de nombres.
Mostrar los nombres en orden alfabético.
Indicar cuántos nombres hay en total.
Buscar si un nombre ingresado por el usuario está en la lista y mostrar un mensaje indicando si se encontró o no.
'''

# Crear una lista vacía
nombres = []

# Solicitar 5 nombres al usuario
print("Ingresa 5 nombres:")
for i in range(5):
    print("Nombre ",i," :")
    nombre = input()
    nombres.append(nombre)

# 1. Mostrar la lista completa
print("\nLista de nombres ingresados:")
print(nombres)

# 2. Mostrar los nombres en orden alfabético
nombres_ordenados = sorted(nombres)
print("\nNombres en orden alfabético:")
print(nombres_ordenados)

# 3. Mostrar cuántos nombres hay
print(f"\nCantidad total de nombres: {len(nombres)}")

# 4. Buscar un nombre en la lista
buscar = input("\nEscribe un nombre para buscar en la lista: ")
if buscar in nombres:
    print(f"{buscar} está en la lista.")
else:
    print(f"{buscar} no se encontró en la lista.")
