import os
os.system("cls")

def tabla (num, inicio, fin):
    
    if inicio > fin:
        return
    resultado = num * inicio
    print ( f"{num} x {inicio} = {resultado}" )
    
    tabla (num, inicio + 1, fin)

numero = int (input ("Número: "))
inicio = int (input ("Inicio: "))
fin = int (input ("Fin: "))

tabla (numero, inicio, fin)