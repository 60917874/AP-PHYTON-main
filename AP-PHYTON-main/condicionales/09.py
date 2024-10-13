import os
os.system("cls")

codigo = int ( input ( "codigo del producto: ") )
unidades = int ( input ( "Unidades: ") )

precioUnitario = 0
descuento = 0

if codigo == 101:
    precioUnitario = 17
    if 1 <= unidades <= 10:
        descuento = 0.05
elif codigo == 102:
    precioUnitario = 25
    if 11 <= unidades <=20:
        descuento = 0.08
elif codigo == 103:
    precioUnitario = 16
    if 21 <= unidades <=30:
        descuento = 0.10
elif codigo == 104:
    precioUnitario = 27
    if unidades >= 31:
        descuento = 0.13

compra = precioUnitario * unidades
descuentoAplicado = compra * descuento
total = compra - descuentoAplicado

print ( f"Importe de la compra: S/. {compra:.2f}" )
print ( f"Descuento: S/. {descuentoAplicado:.2f}" )
print ( f"Total de pago: S/. {total:.2f}" )
