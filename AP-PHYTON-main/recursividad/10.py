import os
os.system("cls")

def eliminarPares (lista):
    if not lista:
        return []
    elif lista [0] % 2 == 0:
        return eliminarPares (lista [1:])
    else:
        return [lista [0]] + eliminarPares (lista [1:])

print (eliminarPares([1, 2, 3, 4, 5]))