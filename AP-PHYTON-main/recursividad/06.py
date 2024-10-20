import os
os.system("cls")

def sumaMatriz (matriz):
    if not matriz:
        return 0
    else:
        return sum (matriz[0]) + sumaMatriz (matriz[1:])

print (sumaMatriz ([[1, 2], [3, 4], [5, 6]]))