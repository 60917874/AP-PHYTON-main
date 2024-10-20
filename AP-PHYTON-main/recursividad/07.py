import os
os.system("cls")

def contarPares (lista):
    if not lista:
        return 0
    elif lista [0] % 2 == 0:
        return 1 + contarPares (lista [1:] )
    else:
        return contarPares (lista [1:] )
    
print (contarPares([1, 2, 3, 4, 5]))