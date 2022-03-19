#1.uzd
from ensurepip import version
from hashlib import shake_128
from ntpath import join
from platform import python_version_tuple
from wsgiref.simple_server import sys_version


print("Mācies, kamēr gudrs tiec,\n  Visu labi vērā liec.\nDzīve gudra, viltīga-\n  Gudrība tur derīga!")

print()
#2.uzd
import sys
from wsgiref.simple_server import sys_version
print(sys_version)

print()
#3.uzd
import math
radius = int(input("Ievadi rinķa radiusu: "))
Rinkalaukums = (math.pi*(radius*radius))
print("Rinķa laukums ir:", Rinkalaukums)

print()
#4.uzd
vards = str(input("Ieraksti savu vārdu:"))
print(vards[::-1])

print()

#10.uzd
print("Man viss izdodas!")

print()

#9.uzd
svars = int(input("Ievadi savu svaru: "))
augums = float(input("Ievadi savu augumu metros: "))
kmi = (svars / ((augums * augums) ))
print("Tavs ķermeņa massas indeks ir: ", kmi)

print()

#7.uzd
sk1 = int(input("Ievadi skaitli x: "))
rezultats = sk1 * sk1 +(sk1 / 2) * 2
print("Rezultāts: ", rezultats)

#6.uzd
people = ["olas", "piens", "siers", "kefirs", "jogurts"]
print(people[0])   
print(people[4])
