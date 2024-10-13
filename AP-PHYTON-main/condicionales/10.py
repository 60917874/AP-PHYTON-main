import os
os.system("cls")

notas = []

for i in range (5):
    nota = float ( input ( f"Nota: ") )
    notas.append(nota)

mayor = max (notas)
menor = min (notas)

print (f"Nota mayor: {mayor}" )
print ( f"Nota menor: {menor}" )

notas.remove (mayor)
notas.remove (menor)

promedio = sum(notas) / len (notas)

print ( f"Promedio: {promedio:.2f}" )