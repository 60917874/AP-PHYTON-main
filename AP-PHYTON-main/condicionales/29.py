import os
os.system("cls")

Htrabajadas = float ( input ( "Horas trabajadas: ") )
pagoHora = float ( input ( "Pago por hora: ") )

if Htrabajadas <= 48:
    sueldoB = Htrabajadas * pagoHora
else:
    Hextras = Htrabajadas - 48
    sueldoB = (48 * pagoHora) + (Hextras * pagoHora* 1.2)
    
if sueldoB > 1500:
    descuento = sueldoB * 0.11
else:
    descuento = 0

total = sueldoB - descuento

print ( f"Horas trabajadas: {Htrabajadas}" )
print ( f"Pago por hora: S/. {pagoHora:.2f}" )
print ( f"Sueldo Bruto: S/. {sueldoB:.2f}" )
print ( f"Descuento: S/. {descuento:.2f}" )
print ( f"Total paga: S/. {total}" )