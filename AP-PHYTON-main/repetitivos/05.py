import os
os.system("cls")

def tabla (n, i = 1):
    
    if i > 12:
        return
    resultado = n * i
    print(f"{n} X {i} = {resultado}")

    tabla(n, i + 1)

numero = int(input("Número: "))
tabla (numero)