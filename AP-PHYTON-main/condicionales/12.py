import os
os.system("cls")

numero = int ( input( "Numero: ") )

if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miercoles"
elif numero == 4:
    dia = "Jueves"
elif numero == 5:
    dia = "Viernes"
elif numero == 6:
    dia = "Sabado"
elif numero == 7:
    dia = "Domingo"
else:
    dia = "Error"

print ( f"Dia: {dia}")