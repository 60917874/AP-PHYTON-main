import os
os.system("cls")

def sumaC(num, posicion, sumaPar, sumaImpar):
    if posicion > 4:  
        if sumaPar == sumaImpar:
            return 1  
        else:
            return 0 
    
    cifra = (num // (10 ** (4 - posicion))) % 10 
    
    if cifra % 2 == 0:
        sumaPar += cifra
    else:
        sumaImpar += cifra
    
    return sumaC(num, posicion + 1, sumaPar, sumaImpar)

def numeros():
    contador = 0 

    for num in range(1000, 10000): 
        if sumaC(num, 1, 0, 0) == 1:
            print(num)
            contador += 1 
    
    return contador

cantidad = numeros()
print(f"Números encontrados: {cantidad}")