import os
os.system("cls")

def multiplos (n, m, contador = 0):
    
    if contador < m:
        print (n * (contador + 1) )
        multiplos (n, m, contador + 1)

numero = int( input("Número: ") )
cantidad = int( input("Cantidad de múltiplos: ") )

multiplos (numero, cantidad)