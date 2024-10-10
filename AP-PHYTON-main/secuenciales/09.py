import os
os.system("cls")

numero = int ( input ( "numero positivo: ") )

millares = numero // 1000
centenas = (numero // 100) % 10
decenas = (numero // 10) % 10
unidades = numero % 10

Scifras = millares + centenas + decenas + unidades

print ( f"Scifras: {Scifras:.2f}")