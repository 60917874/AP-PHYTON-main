import os
os.system("cls")

gigabytes = int (input("Gigabytes: "))
megabytes = gigabytes * 1024

megabytes = gigabytes * 1024
kilobytes = megabytes * 1024
bytes = kilobytes * 1024

print (f"Bytes: {bytes:}")
print (f"Kilobytes: {kilobytes:}")
print (f"Megabytes: {megabytes:}")