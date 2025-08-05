#Inicializar una lista. Crea una lista vacia
l=[]

# Crear una lista
frutas = ["manzana", "plátano", "naranja"]

# Imprimir la lista completa
print("Frutas:", frutas)

# Acceder a un elemento por índice
print("Primera fruta:", frutas[0])  # manzana

# Agregar una fruta al final
frutas.append("uva")

# Insertar en una posición específica
frutas.insert(1, "kiwi")  # Inserta en la posición 1

# Eliminar un elemento por nombre
frutas.remove("plátano")

# Ordenar la lista alfabéticamente
frutas.sort()

#Eliminar el último elemento de la lista
frutas = ["manzana", "plátano", "naranja"]

# Recorrer la lista con un ciclo
print("Lista final de frutas:")
for f in frutas:
    print("-", f)
