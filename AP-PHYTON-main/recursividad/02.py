import os
os.system("cls")

def ordenada (lista):
    if len (lista) <= 1:
        return True
    elif lista [0] > lista [1]:
        return False
    else:
        return ordenada (lista [1:])

print (ordenada ([1, 2, 3, 4, 5]))
print (ordenada ([1, 3, 2]))