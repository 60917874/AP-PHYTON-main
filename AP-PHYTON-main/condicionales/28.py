import os
os.system("cls")

hora = int ( input ( "Hora en formato 24 horas: ") )
minutos = int ( input ( "Minutos: ") )

if 0 <= hora < 24 and 0 <= minutos < 60:
    if hora >= 12:
        formato = hora - 12
        if formato == 0:
            formato = 12
        print ( f"Hora en formato 12 horas: {formato}:{minutos:02d} PM")
    else:
        if hora == 0:
            formato = 12
        else:
            formato = hora
        print ( f"Hora en formato de 12 horas: {formato}:{minutos:02d} AM")
else:
    print ( f"Error. Debe ser una hora valida" )        