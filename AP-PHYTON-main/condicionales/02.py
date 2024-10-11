import os
os.system("cls")

precio = 20
unidades = int ( input ( "Unidades: " ) )

compra = precio * unidades

if compra <= 500 : descuento = 0.12 * compra
elif compra <= 700 : descuento = 0.14 * compra
else: descuento = 0.16 * compra

if unidades <= 50 : caramelos = 5
elif unidades <= 100 : caramelos = 10
else : caramelos = 15

print (f"Compra = {compra:.2f}")
print (f"Descuento = {descuento:.2f}")
print (f"Total  = {(compra - descuento):.2f}")
print (f"Caramelos = {caramelos:.2f}")
