import os
os.system("cls")

def multiplos (n, m):
    contador = 0
    multiplo = n 
    
    while contador < m:
        print(multiplo)
        multiplo += n 
        contador += 1

numero = int(input("Numero : "))
cantidad = int(input("Cantidad de múltiplos: "))

multiplos(numero, cantidad)