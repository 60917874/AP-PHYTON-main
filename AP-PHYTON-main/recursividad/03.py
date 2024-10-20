import os
os.system("cls")

def contarDigitos (n):
    if n < 10:
        return 1
    else: return 1 + contarDigitos (n // 10)

print (contarDigitos (12345))