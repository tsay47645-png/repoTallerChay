'''
A continuación se muestra la estructura de control if. El programa 
1.- Pide al usuario su edad.
2.- Si la edad es 18 o más, muestra: "Eres mayor de edad."
3.- Si la edad está entre 1 y 17, muestra: "Eres menor de edad."
4.- Si se ingresa 0 o un número negativo, muestra: "Edad no válida."
'''

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad > 0:
    print("Eres menor de edad.")
else:
    print("Edad no válida.")