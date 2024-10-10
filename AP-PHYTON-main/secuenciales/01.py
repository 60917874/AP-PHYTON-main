import os
os.system("cls")

varones = int( input("varones :") )
mujeres = int( input("mujeres :") )

total = varones + mujeres
pVarones = varones * 100.0 / total
pMujeres = mujeres * 100.0 / total

print(f"% Varones = {pVarones:.2f} %")
print(f"% Mujeres = {pMujeres:.2f} %")