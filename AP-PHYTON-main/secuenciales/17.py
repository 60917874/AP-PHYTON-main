import os
os.system("cls")

Tdonacion = float (input ("Total de donacion: ") )

Csalud = Tdonacion * 0.25
Cinfantil = Tdonacion * 0.35
Einfantil = Tdonacion * 0.25
Aancianos = Tdonacion * ( 1 - ( 0.25 + 0.35 + 0.25 ) )

print ( f"Csalud: ${Csalud:.2f}" )
print ( f"Cinfantil: ${Cinfantil:.2f}" )
print ( f"Einfantil: ${Einfantil:.2f}" )
print ( f"Aancianos: ${Aancianos:.2f}" )