import os
os.system("cls")

def reemplazarValorMayor (lista, valor):
    if not lista:
        return []
    elif lista [0] > valor:
        return [valor] + reemplazarValorMayor (lista[1:], valor)
    else:
        return [lista[0]] + reemplazarValorMayor (lista [1:], valor)

print ( reemplazarValorMayor([1, 5, 8, 3, 12], 5))