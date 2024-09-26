import random
print("SELAMAT DATANG DI MOBILE LEGEND")
nama_dia = "ARGUS"
cocok = random.random()
print("Kecocokan anda", cocok * 100, "%")
if cocok > 0.8:
    print("Anda sangat cocok dengan midlane " + nama_dia + nama_dia + "!")
elif 0.5 <= cocok <= 0.8:
    print("Anda lumayan cocok dengan explane " + nama_dia + nama_dia + "!")
else:
    print("Anda tidak cocok dengan goldlane " + nama_dia + nama_dia + "!")