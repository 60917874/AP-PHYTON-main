import os
os.system("cls")

Htrabajadas = int ( input ( "Horas trabajadas: "))
Thoraria = int ( input ( "Tarifa horarias: "))

Sbasico = Htrabajadas * Thoraria
Sbruto = Sbasico * 1.20
Sneto = Sbruto * 0.90

print ( f"Sbasico: {Sbasico:.2f}" )
print ( f"Sbruto: {Sbruto:.2f}" )
print ( f"Sneto: {Sneto:.2f}" )