import os
os.system("cls")

a = int ( input ( "Primer Numero: ") )
b = int ( input ( "Segundo Numero: ") )
c = int ( input ( "Tercer Numero: ") )

if a < b < c:
    resultado = "En orden ascendente"
elif a > b > c:
    resultado = "En orden descendente"
else:
    resultado = "En desorden"
    
print (resultado)