import os
os.system("cls")

radio = int ( input ( "radio: " ) )
altura = int ( input ( "altura: ") )

pi = 3.14159

Abase = pi * radio ** 2
Alateral = 2 * pi * radio * altura
Atotal = 2 * Abase * Alateral

print ( f"Abase: {Abase:.2f}" )
print ( f"Alateral: {Alateral:.2f}" )
print ( f"Atotal: {Atotal:.2f}" )