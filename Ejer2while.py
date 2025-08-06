numero = 0
acu=0
cont=0
while numero >= 0 and numero <=100 :
    numero = int(input("Escribelas calificaciones (del 0 al 100, para salir utiliza un número negativo)"))
    if numero>0:
        acu+=numero
        cont+=1
    else:
        print("Terminaste de capturar las calificaciones")
        exit 

if acu!=0:   
    print("total de calificaciones: ",cont)
    print("promedio final: ",(acu/cont))
else:
    print("no ingresaste ninguna calificación válida")
    