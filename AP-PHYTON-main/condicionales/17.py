import os
os.system("cls")

precio = 30
docenas = int ( input ("Cantidad por docenas: ") )

compra = precio * docenas

if docenas >= 6:
    descuento = 0.15 * compra
else:
    descuento = 0.10 * compra

Tpaga = compra - descuento

if docenas >= 30:
    lapiceros = (docenas // 3) * 2
else:
    lapiceros = 0
    
print ( f"Monto de compra: S/. {compra:.2f}" )
print ( f"Descuento: S/. {descuento:.2f}" )
print ( f"Total pagar: S/. {Tpaga}" )
print ( f"Lapiceros: {lapiceros}" )