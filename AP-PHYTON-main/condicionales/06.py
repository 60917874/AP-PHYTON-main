import os
os.system

primeraEdad = int ( input ( "Primera edad: ") )
segundaEdad = int (input ( "Segunda edad: ") )
terceraEdad = int ( input ( "Tercera edad: ") )

menor = min (primeraEdad, segundaEdad, terceraEdad)
mayor = max (primeraEdad, segundaEdad, terceraEdad)

print ( f"Edad menor: {menor}" )
print ( f"Edad mayor: {mayor}" )