import os
os.system("cls")

Pnumero = input ( "Primer numero: ")
Snumero = input ( "Segundo numero: ")

Cifra1 = Snumero [0] + Pnumero [1] + Snumero [2]
Cifra3 = Pnumero [0] + Snumero [1] + Pnumero [2]

print ( f"Cifra1: {Cifra1:}" )
print ( f"Cifra3: {Cifra3:}" )