import os
os.system("cls")

def maximo (lista):
    if len (lista) == 1:
        return lista [0]
    else:
        maximoResto = maximo (lista[1:])
        return lista [0] if lista [0] > maximoResto else maximoResto

print (maximo([3, 5, 2, 9, 1]))