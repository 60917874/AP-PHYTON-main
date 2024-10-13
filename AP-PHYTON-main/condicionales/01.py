import os
os.system("cls")

unidades = int( input ( "Unidades: ") )

if 1 <= unidades <= 25:
    precioUnitario = 27
elif 26 <= unidades <= 50:
    precioUnitario = 25
else:
    precioUnitario = 23

compra = precioUnitario * unidades

if unidades > 50:
    descuento = 0.15 * compra
else:
    descuento = 0.05 * compra

total = compra - descuento

print( f"Compra: S/. {compra:.2f}" )
print( f"Descuento: S/. {descuento:.2f}" )
print( f"Total: S/. {total:.2f}")