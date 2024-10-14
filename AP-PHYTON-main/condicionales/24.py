import os
os.system("cls")

vendido = float ( input ( "Total Vendido: ") )

sueldoBasico = 0.10 * vendido

if vendido > 5000:
    exceso = vendido - 5000
    bono = int (exceso // 500) * 25
else:
    bono = 0

sueldoTotal = sueldoBasico + bono

print ( f"Sueldo Basico: S/. {sueldoBasico:.2f}" )
print ( f"Bono en Exceso: S/. {bono:.2f}" )
print ( f"Sueldo Total: S/. {sueldoTotal:.2f}" )