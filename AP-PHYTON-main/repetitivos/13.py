import os
os.system("cls")

def suma (n, actual=1):
    if actual > n:
        return 0
    
    if actual % 3 == 0 and actual % 5 != 0:
        return actual + suma(n, actual + 1)
    
    return suma (n, actual + 1)

numero = int ( input("Numero: "))

resultado = suma (numero)
print ( f"La suma de los múltiplos de 3 menores o iguales a {numero} es: {resultado}")