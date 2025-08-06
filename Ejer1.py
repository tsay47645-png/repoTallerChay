edad = int(input("Ingresa la edad del cliente: "))

if edad < 4:
    print("No pagas un boleto es gratis")
elif edad > 4 and edad <= 12:
    print("Pagas un boleto infantil, costo: $40 pesos")
elif edad > 12 and edad <= 59:
    print("Pagas un boleto general, costo: $70 pesos")
else:
    print("Pagas un boleto de adulto mayor, costo: $35 pesos")
