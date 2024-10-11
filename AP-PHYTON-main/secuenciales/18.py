import os
os.system("cls")

cantidad = int ( input ( "Cantidad de unidad: ") )
Punitario = int ( input ( "Precio unitario: ") )

importe = cantidad * Punitario
descuento1 = 0.15 * importe
descuento2 = 0.15 * ( importe - descuento1 )
Paga = descuento1 + descuento2

print ( f"importe: ${importe:.2f}" )
print ( f"Total: ${descuento1 + descuento2:.2f}" )
print ( f"Paga: ${Paga:.2f}")