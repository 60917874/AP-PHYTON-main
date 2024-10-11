import os
os.system("cls")

Sbasico = 500
montoT = int ( input ( "Monto Total: ") )

comision = montoT * 0.09
Sbruto = Sbasico + comision
descuento = Sbruto * 0.11
Sneto = Sbruto - descuento

print ( f"Comision: S/. {comision:.2f}" )
print ( f"Sbruto: S/. {Sbruto:.2f}" )
print ( f"Descuento: S/. {descuento:.2f}" )
print ( f"Sneto: S/. {Sneto:.2f}" )