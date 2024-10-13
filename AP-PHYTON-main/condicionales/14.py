import os
os.system("cls")

Ntarjeta = int ( input ( "Numero de tarjeta: ") )
Mcompra = float ( input ( "Monto: ") )

if Ntarjeta % 2 == 0 and Ntarjeta >= 100:
    descuento = 0.15 * Mcompra
else:
    descuento = 0.05 * Mcompra

print ( f"Numero de Tarjeta: {Ntarjeta}" )
print ( f"Monto: {Mcompra:.2f}" )
print ( f"Descuento: {descuento:.2f}" )