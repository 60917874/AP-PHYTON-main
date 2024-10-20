import os
os.system("cls")

def dibujar (altura):
    ancho = 2 * altura
    for _ in range (altura):
        print ('*' * ancho)

n = int ( input("Altura: ") )

if n >= 4:
    dibujar (n)
else:
    print( "Debe ser al menos 4." )