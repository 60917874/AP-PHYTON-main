import os
os.system("cls")
import math

numeros = []
for i in range(5):
    numero = int ( input ( "numero: ") )
    numeros.append (numero)

numeros.sort(reverse=True)
mayor = numeros [:3]

promedio = sum (mayor) / len (mayor)

print ( f"promedio: {promedio:.2f}" )