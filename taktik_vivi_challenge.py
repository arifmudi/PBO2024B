print ("Nama : vivi damayanti")
print ("Nim : 2355201025")

#TACTICAL DOLL KITA
print ("### MY TECTICAL DOLL ###")
nama_tactical_doll = input("Masukkan Nama Tactical Dollmu : ")
firepower = int(input("Damage firepower : "))
rate_of_fire = int(input("Jumlah Rate Of fire : "))
accuracy = int(input("Jumlah Accuracy : "))
evasion = int(input("Masukkan Evasion : "))
damage_per_second = round(firepower * rate_of_fire/60,2)
combat_effectiveness = int (30 * float(firepower) +(40 * (float(rate_of_fire) ** 2) / 120) +(15 *(accuracy+evasion)))


#TACTICAL DOLL MUSUH
print ("### ENEMY TECTICAL DOLL ###")
nama_tactical_doll_musuh = input("Masukkan Nama Tactical Doll Musuh : ")
firepower_musuh = input("Damage firepower Musuh : ")
rate_of_fire_musuh = input("Jumlah Rate Of fire Musuh : ")
accuracy_musuh = input("Jumlah Accuracy Musuh : ")
evasion_musuh = input("Masukkan Evasion Musuh : ")
damage_per_second_musuh = round (float(firepower_musuh) * float(rate_of_fire_musuh)/60,2)
combat_effectiveness_musuh = int (30 * float(firepower_musuh) +(40 * float(rate_of_fire_musuh) ** 2) / 120 +
                                  15 * (float(accuracy_musuh) + float(evasion_musuh)))

#KEPUTUSAN
power_doll = damage_per_second + combat_effectiveness
power_doll_musuh = damage_per_second_musuh + combat_effectiveness_musuh

print ("### RESULT ###")
print (nama_tactical_doll)
print ("damage_per_second : " + str(damage_per_second))
print ("combat Effecttiveness : " + str(combat_effectiveness))
print (nama_tactical_doll_musuh)
print ("Damage per second : " + str(damage_per_second_musuh))
print ("combat Effecttiveness :" + str(combat_effectiveness_musuh))

#LANGKAH YANG DIAMBIL
if power_doll > power_doll_musuh:
    print ("Keputusan : Gassss polll")
elif power_doll < power_doll_musuh:
    print ("Keputusan : susah banget musuhnyaa")
else :
    print ("sama nihhh")