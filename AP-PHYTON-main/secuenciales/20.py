import os
os.system("cls")

cantidad = int ( input ( "Dinero en Soles: S/. ") )

ByM = [200,100,50,20,10,5,2,1]

desglose = {}

for valor in ByM:
    if cantidad >= valor:
        billetes = cantidad // valor
        desglose[valor] = billetes
        cantidad -= billetes * valor

for valor, cantidad in desglose.items():
    if valor >= 10:
        print ( f"{cantidad} billetes de S/. {valor}")
    else:
        print ( f"{cantidad} monedad de S/. {valor}")