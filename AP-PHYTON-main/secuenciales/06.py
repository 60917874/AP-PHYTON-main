import os
os.system("cls")

radio = int ( input ( "Radio: ") )
altura = int ( input ( "Altura: ") )

pi= 3.14159

aréaT = 2 * pi * radio
areaT= radio + altura
volumen = pi * radio ** 2 * altura

print ( f"areaT: {areaT:.2f}" )
print ( f"volumen: {volumen:.2f}" )