import os
os.system("cls")

dividendo = int ( input ( "Dividendo: ") )
divisor = int ( input ( "Divisor: ") )

cociente = 0
while dividendo >= divisor:
    cociente += 1
    dividendo -= divisor

print (f"Cociente = {cociente}" )
print (f"Residuo = {dividendo}" )