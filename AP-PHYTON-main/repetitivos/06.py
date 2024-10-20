import os
os.system("cls")

def tabla (num, inicio, fin):
    for i in range(inicio, fin + 1):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")

numero = int(input("Numero: "))
inicio = int(input("inicio: "))
fin = int(input("Fin: "))

tabla (numero, inicio, fin)