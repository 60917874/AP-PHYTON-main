import os
os.system("cls")

pies = int (input("pies: "))
pulgadas = int (input("pulgadas: "))

tpulgadas = pies * 12 + pulgadas 
centimetros = tpulgadas * 2.54
metros = centimetros / 100

print (f"metros: {metros:.2f}")