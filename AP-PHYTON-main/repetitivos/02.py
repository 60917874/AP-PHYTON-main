import os
os.system("cls")

def multiplicar (n1, n2):
    producto = 0
    while n2 > 0:
        n2 -= 1
    producto += n1
    return producto

def multiplica (n1, n2):
    if n2 == 1:  return n1
    return multiplica (n1, n2 - 1)

multiplicando = int ( input ( "Multiplicando: ") )
multiplicador = int ( input ( "Multiplicador: ") )

print ( f"Producto = {multiplicar (multiplicando, multiplicador)}")