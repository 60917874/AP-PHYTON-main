import os
os.system("cls")

def imprimir (numero, limite, fila):
    print (numero, end="\t")
    
    if numero % fila == 0:
        print ()

    if numero < limite:
        imprimir (numero + 1, limite, fila)

imprimir (1, 100, 10)