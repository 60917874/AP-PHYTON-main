import os
os.system("cls")

n = int ( input ("Numero: ") )
m = int ( input ( "Cantidad de Multiples: ") )

def multiplos (n, m):
    for i in range (1, m + 1):
        print (n * i)

print ( f"Los {m} multiplos de {n} son:" )
multiplos(n, m)