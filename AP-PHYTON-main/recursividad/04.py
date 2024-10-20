import os
os.system("cls")

def sumaDigitos (n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumaDigitos (n // 10)
    
print ( sumaDigitos (123) )