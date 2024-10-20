import os
os.system("cls")

def contarDivisores(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0: 
            contador += 1
    return contador

numero = int(input("Numero entero: "))

cantidad = contarDivisores(numero)

print(f"Cantidad de divisores de {numero} es: {cantidad}")