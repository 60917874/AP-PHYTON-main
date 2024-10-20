import os
os.system("cls")

def Cnegativos( lista ):
    if not lista:
        return 0
    elif lista [0] < 0:
        return 1 + Cnegativos( lista [1:] )
    else:
        return Cnegativos ( lista [1:] )
    
print (Cnegativos([1, -2, 3, -4, 5]))