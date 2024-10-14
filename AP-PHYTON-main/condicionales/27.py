import os
os.system("cls")

sueldo = 600
vendido = float ( input ( "Monto vendido: ") )

comision = 0.15 * vendido
sueldoB = sueldo + comision

if sueldoB > 1800:
    descuento = 0.10 * sueldoB
else:
    descuento = 0.05 * sueldoB
    
sueldoN = sueldoB - descuento

if vendido > 1000:
    polos = 3
else:
    polos = 1
    
print ( f"Sueldo Bruto: S/. {sueldoB:.2f}" )
print ( f"Descuento: S/. {descuento:.2f}" )
print ( f"Sueldo Neto: S/. {sueldoN:.2f}" )
print ( f"Numero de Polos: {polos}" )