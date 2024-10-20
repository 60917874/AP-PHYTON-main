import os
os.system("cls")

def capicua (num, posicion):
    
    numero = str(num)
    
    if posicion >= len(numero) // 2:
        return True
    
    if numero [posicion] != numero[-(posicion + 1)]:
        return False
    
    return capicua (num, posicion + 1)

def contarCapicuas(inicio, fin):
    contador = 0
    for num in range (inicio, fin + 1):
        if capicua(num, 0):
            contador += 1
            print (num)
    return contador

inicio = 100
fin = 999

cantidad = contarCapicuas (inicio, fin)
print ( f"Cantidad de  capicúas: {cantidad}" )