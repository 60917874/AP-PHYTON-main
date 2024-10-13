import os
os.system("cls")

donacion = float ( input ( "Monto de donacion: ") )

if donacion >= 10000:
    Csalud = 0.30 * donacion
    comedor = 0.50 * donacion
    inversion = donacion - (Csalud + comedor)
else: 
    Csalud = 0.25 * donacion
    comedor = 0.60 * donacion
    inversion = donacion - (Csalud + comedor)

print ( f"Monto de Centro de Salud: S/. {Csalud:.2f}" )
print ( f"Monto de Comedor de Niños: S/. {comedor:.2f}" )
print ( f"Monto de lo invertido: S/. {inversion:.2f}" )