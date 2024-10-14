import os
os.system("cls")

cuota = float ( input ( "Cuota Mensual: ") )
pago = int ( input ( "Dia de pago: ") )

if pago <= 10:
    descuento = max (5, 0.02 * cuota)
    monto = cuota - descuento
else:
    if pago <= 20:
        monto = cuota
    else:
        recargo = max (10, 0.3 * cuota)
        monto = cuota + recargo

print ( f"Monto a pagar: S/. {monto:.2f}" )