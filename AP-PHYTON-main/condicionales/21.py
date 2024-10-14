import os
os.system("cls")

numero = int ( input ( "Numero: ") )

if 1000 <= numero <= 9999:
    estadoCivil = numero // 1000
    edad = (numero // 10) % 100
    sexo = numero % 10
    
    if estadoCivil == 1:
        categoriaEstadoCivil = "Soltero"
    elif estadoCivil == 2:
        categoriaEstadoCivil = "Casado"
    elif estadoCivil == 3:
        categoriaEstadoCivil = "Divorciado"
    elif estadoCivil == 4:
        categoriaEstadoCivil = "Viudo"
    else:
        categoriaEstadoCivil = "Error"
        
    if sexo == 1:
        categoriaSexo = "Masculino"
    elif sexo == 2:
        categoriaSexo = "Femenino"
    else:
        categoriaSexo = "Error"
    
    print ( f"Estado Civil: {categoriaEstadoCivil}" )
    print ( f"Edad: {edad}" )
    print ( f"Sexo: {categoriaSexo}" )
else:
    print ("Error. Debe ser nunmero positivo de 4 cifras")