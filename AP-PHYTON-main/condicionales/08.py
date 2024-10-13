import os
os.system("cls")

propina = 20
examenAprobado = int ( input ( "Examenes Aprobados: ") )

if examenAprobado > 3:
    print ( "Examenes no aprobados: " )
else:
    propinaAdicional = examenAprobado * 5
    total = propina + propinaAdicional
    
print ( f"Total de propina: S/. {total:.2f}" )