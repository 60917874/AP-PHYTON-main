import os
os.system("cls")

horasAusencia = float ( input ( "Horas Ausencia: ") )
tornillosMalos = int ( input ( "Tornillos Malos: ") )
tornillosBuenos = float ( input ( "Tornillos Buenos: ") )

if not horasAusencia and not tornillosMalos and not tornillosBuenos: print ( "Grado 5")
if horasAusencia and not tornillosMalos and not tornillosBuenos: print ( "Grado 7")
if not horasAusencia and tornillosMalos and not tornillosBuenos: print ( "Grado 8")
if not horasAusencia and not tornillosMalos and  tornillosBuenos: print ( "Grado 9")
if horasAusencia and tornillosMalos and not tornillosBuenos: print ("Grado 12")
if horasAusencia and not tornillosMalos and tornillosBuenos: print ("Grado 13")
if not horasAusencia and tornillosMalos and tornillosBuenos: print ("Grado 15")
if horasAusencia and tornillosMalos and tornillosBuenos: print ("Grado 20")