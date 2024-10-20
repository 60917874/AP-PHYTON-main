import os
os.system("cls")

def tabla(n):
    for i in range (1, 13):
        resultado = n * i
        print (f"{n} X {i} = {resultado}")

numero = int ( input ("Numero: ") )

tabla(numero)