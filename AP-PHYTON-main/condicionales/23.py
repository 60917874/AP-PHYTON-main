import os
os.system("cls")

matematica = float ( input ( "Nota de Matematica: ") )
fisica = float ( input ( "Nota de Fisica: ") )

if matematica > 17:
    propinaM = 3
else:
    propinaM = matematica

if fisica > 15:
    propinaF = 2
else:
    propinaF = 0.5

promedio = (matematica + fisica) / 2
Totalpropina = propinaM + propinaF

if promedio > 16:
    obsequio = "Obesequia un reloj"
else:
    obsequio = "No se obsequia"

print ( f"Propina de Matematica: S/. {propinaM:.2f}" )
print ( f"Propina de Fisica: S/. {propinaF:.2f}" )
print ( f"Propina Total: S/. {Totalpropina}" )
print (obsequio)