import os
os.system("cls")

ingresoMensual = int ( input ( "Ingreso Mensual: S/. ") )
costoCasa = int ( input ( "Costo Casa: S/. ") )

if ingresoMensual <= 1250 :
    cuotaInicial = 0.15 * costoCasa
    cuotaMensual = ( 0.85 * costoCasa ) / 120
else:
    cuotaInicial = 0.30 * costoCasa
    cuotaMensual = ( 0.70 * costoCasa ) / 120

print ( f"Cuota Inicial: S/. {cuotaInicial:.2f}" )
print ( f"Cuota Mensual: S/. {cuotaMensual:.2f}" )