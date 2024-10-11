import os
os.system("cls")
import math

a = int ( input ( "valor a: "))
b = int ( input ( "valor b: "))
c = int ( input ( "valor c: "))

discriminante = b ** 2 - 4 * a * c

if discriminante > 0:
    r1 = (-b + math.sqrt(discriminante)) / (2 * a)
    r2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print ( f"raices: {r1} & {r2}")
elif discriminante == 0:
    r = -b / (2 * a)
    print ( f"raiz: {r}")
else:
    Vreal = -b / (2 * a)
    Vfalso = math.sqrt(-discriminante) / (2 * a)
    print ( f"raices: {Vreal} + {Vfalso}i & {Vreal} - {Vfalso}i" )