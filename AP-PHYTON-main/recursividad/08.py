import os
os.system("cls")

def sumaImpares (lista, index = 0):
    if not lista:
        return 0
    elif index % 2 == 1:
        return lista [0] + sumaImpares ( lista[1:], index + 1 )
    else:
        return sumaImpares (lista[1:], index + 1)
    
print ( sumaImpares ([1, 2, 3, 4, 5]))