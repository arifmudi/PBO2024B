import random

print("selamat datang di lovemeter")

nama_dia="azhar fajri "
cocok=random.random()

print("kecocokan anda", cocok * 100, "%")
if cocok> 0.8:
    print ("anda sangat cocok dengan "+ nama_dia + "!")
elif 0.5 <= cocok <=0.8:
    print("anda lumayan cocok dengan" + nama_dia +"!")
else :
    ("anda tidak cocok dengan" + nama_dia + "!")
 

 