import os
os.system("cls")

primerNumero = int ( input ( "Primer Numero: ") )
segundoNumero = int ( input ( "Segundo Numero: ") )
tercerNumero = int ( input ( "Tercer Numero: ") )

if (primerNumero > segundoNumero and primerNumero < tercerNumero) or (primerNumero < segundoNumero and primerNumero > tercerNumero):
    intermedio = primerNumero
elif (segundoNumero > primerNumero and segundoNumero < tercerNumero) or (segundoNumero < primerNumero and segundoNumero > tercerNumero):
    intermedio = segundoNumero
else:
    intermedio = tercerNumero

print ( f"Numero Intermedio: {intermedio}" )