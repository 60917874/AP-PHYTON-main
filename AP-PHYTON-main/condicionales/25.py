import os
os.system("cls")

sueldoB = float ( input ( "El sueldo bruto: ") )
Nhijos = int ( input ( "Numero de hijos: ") )

if Nhijos > 1:
    bonificacion = (12.5 / 100) * sueldoB + (40 * Nhijos)
else:
    bonificacion = (10 / 100) * sueldoB

sueldoN = sueldoB + bonificacion

print ( f"Bonificacion: S/. {bonificacion:.2f}" )
print ( f"Sueldo Neto: S/. {sueldoN:.2f}" )