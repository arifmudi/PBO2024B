import random
print("SELAMAT DATANG DI LOVEMETER")
nama_dia = " taehyung"
cocok = random.random()
print("kecocokan anda ", cocok * 100, "%")
if cocok > 0.8:
    print("widia sangat cocok dengan" + nama_dia + "!")
elif 0.5 <= cocok <=0.8:
    print("widia lumayan cocok dengan" + nama_dia + "!")
else:
    print("widia tidak cocok dengan" + nama_dia + ":(")   