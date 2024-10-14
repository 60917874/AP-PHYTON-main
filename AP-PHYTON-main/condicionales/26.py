import os
os.system("cls")

compra = float ( input ( "Monto total: ") )

if compra > 5000:
    porcentaje = 30
else:
    porcentaje = 20

prestamo = (porcentaje / 100) * compra
interes = 0.10 * prestamo
dineroPropio = compra - prestamo

print ( f"Prestamo: ${prestamo:.2f}" )
print ( f"Interes: ${interes:.2f}" )
print ( f"Pago propio: ${dineroPropio:.2f}" )
print ( f"Total paga: ${prestamo + interes + dineroPropio:.2f}" )