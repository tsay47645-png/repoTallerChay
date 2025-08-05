'''este programa pide números del teclado y los muestra en pantalla mi
mietras que el usuario no presione el número cero'''

print("\nCiclo while: escribe números (0 para salir)")
numero = None
while numero != 0:
    numero = int(input("Escribe un número: "))
    print("Escribiste:",numero)
print("Terminaste el ciclo.")