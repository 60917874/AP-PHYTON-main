import os
os.system("cls")

def imprimir(ancho):
    print ('*' * ancho)

def asteriscos (altura, ancho, contador=0):
    if contador < altura:
        imprimir (ancho)
        asteriscos(altura, ancho, contador + 1)

def main():
    n = int (input ("Altura: "))
    if n >= 4:
        ancho = 2 * n 
        asteriscos(n, ancho)
    else:
        print("Debe ser al menos 4")

main()