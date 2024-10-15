import os
os.system("cls")

categoria = input ("Categoria del trabajador: " )
Htrabajadas = float ( input ( "Horas Trabajadas: ") )

if categoria == "A":
    tarifaH = 21.0
elif categoria == "B":
    tarifaH = 19.5
elif categoria == "C":
    tarifaH = 17.0
elif categoria == "D":
    tarifaH = 15.5
else:
    print ("Error")
    tarifa = 0

sueldoB = Htrabajadas * tarifaH

if sueldoB > 2500:
    descuento = sueldoB * 0.20
else:
    descuento = sueldoB * 0.15
    
sueldoN = sueldoB - descuento

print ( f"Sueldo Bruto: S/. {sueldoB:.2f}" )
print ( f"Descuento: S/. {descuento:.2f}" )
print ( f"Sueldo Neto: S/. {sueldoN:.2f}" )