import os
os.system("cls")

def divisores (numero):
    contador = 0
    for i in range (1, numero + 1):
        if numero % i == 0:
            contador += 1
    return contador

numero = int ( input ("Numero entero: ") )

print ( f"Cantidad de divisores {numero} es: {divisores(numero)}")