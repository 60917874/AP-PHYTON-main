import os
os.system("cls")

def primo (num, divisor = None):
    if num < 2:
        return False
    
    if divisor is None:
        divisor = 2

    if divisor * divisor > num:
        return True
    
    if num % divisor == 0:
        return False

    return primo (num, divisor + 1)

numero = int ( input("Numero: ") )

if primo(numero):
    print (f"{numero} número primo")
else:
    print (f"{numero} no es número primo")