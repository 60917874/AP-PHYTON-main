import os
os.system("cls")

def mayusculas(cadena, indice=0):
    if indice >= len (cadena):
        return ""
    
    letraMayuscula = cadena[indice].upper()
    return letraMayuscula + mayusculas(cadena, indice + 1)

def minusculas (cadena, indice=0):
    if indice >= len(cadena):
        return ""
    
    letraMinuscula = cadena[indice].lower()
    return letraMinuscula + minusculas (cadena, indice + 1)

texto = input("Texto: ")

textoMayusculas = mayusculas(texto)
textoMinusculas = minusculas(texto)

print (f"Texto en mayúsculas: {textoMayusculas}")
print (f"Texto en minúsculas: {textoMinusculas}")