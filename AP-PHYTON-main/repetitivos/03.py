import os
os.system("cls")

def divisores (numero, divisor=1):
    if divisor > numero:
        return 0
    
    if numero % divisor == 0:
        return 1 + divisores (numero, divisor + 1)
    else:
        return divisores (numero, divisor + 1)

numero = int(input("Número: "))
cantidad = divisores (numero)

print(f"Cantidad de divisores de {numero} es: {cantidad}")