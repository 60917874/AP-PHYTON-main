import os, math
os.system("cls")

radio = int ( input ( "Radio: ") )
altura = int ( input ( "Altura: ") )

areaT = 2 * math.pi * radio ( radio + altura )
volumen = math.pi * math.pow ( radio,2 ) * altura

print ( f"areaT: {areaT:.2f}" )
print ( f"volumen: {volumen:.2f}" )