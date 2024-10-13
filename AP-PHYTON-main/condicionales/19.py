import os
os.system("cls")

sexo = input ( "Sexo: " )
edad = int ( input ( "Edad: ") )

if sexo == "F":
    if edad < 23:
        categoria = "FA"
    else:
        categoria = "FB"
elif sexo == "M":
    if edad < 25:
        categoria = "MA"
    else:
        categoria = "MB"
else:
    categoria = "Error."
    
print ( f"Categoria: {categoria}")