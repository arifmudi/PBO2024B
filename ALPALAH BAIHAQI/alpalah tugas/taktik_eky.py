print("### REQUES TACTICAL DOLL")
alpalah =input("masukkan arlian tactical doll :")
alpalah1 =input("masukan firepower :")
alpalah2 =input("masukan rate of fire:")
alpalah3 =input("masukan acuracy:")
alpalah4 =input("masukan evasion")
damage_per_second= round(float(alpalah) * float(alpalah2)/60,2)
combat_effectiveness= int(30 * float(alpalah1)+(40*(float(alpalah2)**2)/120) + (15*(float(alpalah3) + float(alpalah4))))

print("### SUCCES ###")
print("tactical doll : " + str(alpalah))
print("fire power : " + str(alpalah1))
print("rate of fire : " + str(alpalah2))
print("accuracy :" + str(alpalah3))
print("evasion :" + str(alpalah4))
print("damage per second : " + str(damage_per_second))
print("combat effectivensss : " + str(combat_effectiveness))