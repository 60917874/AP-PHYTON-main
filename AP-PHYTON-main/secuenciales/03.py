import os
os.system("cls")

kilometros = int (input( "primer tramo: "))
pies = int (input ( "segundo tramo: "))
millas = int (input ( "tercer tramo: ")) 

tmetros = kilometros * 1000
millas = millas * 1609
tyardas = tmetros * 1.0936

print (f"tmetros: {tmetros:.2f}")
print (f"tyardas: {tyardas:.2f}")