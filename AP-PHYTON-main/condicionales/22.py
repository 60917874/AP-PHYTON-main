import os
os.system("cls")

precioA = 25
precioB = 30

unidadA = int ( input ( "Unidad A: ") )
unidadB = int ( input ( "Unidad B: ") )

ImporteA = precioA * unidadA
importeB = precioB * unidadB
importeTotal = ImporteA + importeB

if unidadA > 50:
    descuentoA = 0.15 * ImporteA
else:
    descuentoA = 0

if unidadB > 60:
    descuentoB = 0.10 * importeB
else:
    descuentoB = 0

totalDescuento = descuentoA + descuentoB
pagar = importeTotal - totalDescuento

print ( f"Importe Bruto: S/. {importeTotal:.2f}" )
print ( f"Descuento Total: S/. {totalDescuento:.2f}" )
print ( f"Total paga: S/. {pagar:.2f}" )