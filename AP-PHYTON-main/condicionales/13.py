import os
os.system("cls")

numero = int ( input ( "Numero entero:") )

if 100 <= numero <= 999:
    cifra1 = numero // 100
    cifra2 = (numero // 10) % 10
    cifra3 = numero % 10
    
    if (cifra1 + 1 == cifra2 and + cifra2 + 1 == cifra3) or (cifra1 - 1 == cifra2 and cifra2 - 1 == cifra3):
        resultado = "Son consecutivas."
    else:
        resultado = "No son consecutivas."
else:
    resultado = "Error. Debe ser un numero positivo"

print(resultado)