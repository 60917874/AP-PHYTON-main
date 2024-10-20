import os
os.system("cls")

def factorial (n):
    rpta = 1
    while n > 1:
        rpta *= n
        n -= 1

    return rpta

def factorial_r (n):
    if n == 1: return 1
    return n * factorial_r (n - 1)

numero = int (input ( "Numero: ") )

print (f"Factorial: {factorial_r(numero)}")