import os
os.system("cls")

juan = int ( input ( "Aporte de Juan en dolares: "))
rosa = int ( input ( "Aporte de Rosa en dolares: "))
daniel = int ( input ( "Aporte de Daniel en soles: "))

tasa = 3.00

aporte = daniel / tasa
capitalT = juan + rosa + aporte

Pjuan = (juan / capitalT) * 100
Prosa = (rosa / capitalT) * 100
Pdaniel = (aporte / capitalT) * 100

print ( f"capitalT: ${capitalT:.2f}")
print ( f"Pjuan: {Pjuan:.2f}%")
print ( f"Prosa: {Prosa:.2f}%")
print ( f"Pdaniel: {Pdaniel:.2f}%")