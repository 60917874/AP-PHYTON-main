import os
os.system("cls")
import math

a = int ( input ( "cateto 1: "))
b = int ( input ( "cateto 2: "))

hipotenusa = math.sqrt( a ** 2 + b ** 2 )

print ( f"hipotenusa: {hipotenusa:.2f}" )