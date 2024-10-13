import os
os.system("cls")

practica1 = int ( input ( "Primera Nota: ") )
practica2 = int ( input ( "Segunda Nota: ") )
practica3 = int ( input ( "Tercera Nota: ") )

if practica3 >= 10:
    practica3 += 2

promedio = (practica1 + practica2 + practica3) / 3

print ( f"Promedio Final es: {promedio:.2f}" )