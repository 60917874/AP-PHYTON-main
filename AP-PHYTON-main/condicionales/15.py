import os
os.system("cls")

sueldoBasico= 250
vendido = float ( input ( "Monto vendido total: ") )

if vendido <= 5000:
    comision = 0.05 * vendido
elif vendido <= 10000:
    comision = 0.07 * vendido
else:
    comision = 0.10 * vendido

sueldoBruto = sueldoBasico + comision

if sueldoBruto > 3500:
    descuento = 0.15 * sueldoBruto
else:
    descuento = 0.08 * sueldoBruto

sueldoNeto = sueldoBruto - descuento

print ( f"Sueldo Bruto: S/. {sueldoBruto:.2f}" )
print ( f"Comision: S/. {comision:.2f}" )
print ( f"Descuento: S/. {descuento:.2f}" )
print ( f"Sueldo Neto: S/. {sueldoNeto:.2f}" )