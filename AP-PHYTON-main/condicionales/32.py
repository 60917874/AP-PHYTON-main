import os
os.system("cls")

categoria = input ( "Categoria: " )
promedio = float ( input ("Promedio del ciclo: ") )

if categoria == "A":
    pension = 550
elif categoria == "B":
    pension = 500
elif categoria == "C":
    pension = 450
elif categoria == "D":
    pension = 400
else:
    print ( "Error" )
    pension = 0

if 0 <= promedio <= 13.99:
    descuento = 0
elif 14 <= promedio <= 15.99:
    descuento = 0.10
elif 16 <= promedio <= 17.99:
    descuento = 0.12 * pension
elif 18 <= promedio <= 20:
    descuento = 0.15 * pension
else:
    print ( "Error")
    descuento = 0

pensionN = pension - descuento

print ( f"Pension Actual: S/. {pension:.2f}" )
print ( f"Descuento: S/. {descuento:.2f}" )
print ( f"Pension Nueva: S/. {pensionN:.2f}" )