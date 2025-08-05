
import numpy as np


#crear un arreglo con diez elementos del 0-9
numeros=np.arange(10)
#crea un arreglo de 15 elementos en el rango de 15-20
numeros=np.arange(5,20)
# Crear un arreglo (array) de NumPy
numeros = np.array([1, 2, 3, 4, 5])

# Mostrar el arreglo
print("Array original:", numeros)

# Sumar 10 a cada elemento
suma = numeros + 10
print("Suma +10:", suma)

# Calcular estadísticas
print("Media:", np.mean(numeros))
print("Suma total:", np.sum(numeros))
print("Valor máximo:", np.max(numeros))
print("Valor mínimo:", np.min(numeros))

# Crear una matriz 2x3
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz 2x3:\n", matriz)

# Transponer la matriz
print("Matriz transpuesta:\n", matriz.T)

#crea un vector de 20 números enteros aleatorios en el rango del 1-20
x=np.random.randint(1,10,20)

#convierte el vector de 20 elementos a una matriz de 4x5
x=np.reshape(x,[4,5])

