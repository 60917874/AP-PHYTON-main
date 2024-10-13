import os
os.system("cls")

numero = input ( "Numero de 4 cifras: ")

if len(numero) != 4 or not numero.isdigit():
    print ( "Numero no valido: ")
else:
    cifras = [int(digito) for digito in numero]
    cifraMayor = max(cifras)
    cifraMenor = min(cifras)
    
    mayor = cifraMayor * 10 + cifraMenor

    print ( f"Mayor numero: {mayor}" )