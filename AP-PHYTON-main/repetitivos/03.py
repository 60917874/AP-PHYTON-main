import os
os.system("cls")

numero = int ( input ("Numero entero: ") )

def divisores (numero):
    contador = 0
    for i in range (1, numero + 1):
        if numero % i == 0:
            contador += 1
    return contador

print ( f"Cantidad de divisores {numero} es: {divisores(numero)}")