print ("nama : salsabillah rahmadhani")
print ("Nim : 2355201038")

#TACTICAL DOLL KITA
print ("### MY TECTICAL DOLL ###")
nama_tectical_doll = input ("masukan nama tectical dollmu : ")
firepower = int(input("damage firepower : "))
rate_of_fire = int(input("jumlah rate_of_fire"))
accuracy = int(input("jumlah accuracy"))
evasion = int(input("masukan evasion"))
damage_per_second = round (firepower * rate_of_fire/60,2)
combat_effectiveness = int (30 * float(firepower) + (40 *(float(rate_of_fire) ** 2)/120) +(15 *(accuracy+evasion)))

#TACTICAL DOLL MUAUH 
print("### ENEMY TACTICAL DOLL ###")
nama_tectical_doll_musuh = input ("Masukkan Nama Tactical Doll Musuh : ")
firepower_musuh = input ("Damage Direpower Musuh : ")
rate_of_fire_musuh = input ("jumlah rate of fre musuh : ")
accuracy_musuh = input ("jumlah accuracy musuh ")
avasion_musuh = ("masukkan avasion musuh :")
demage_per_second_musuh = round (float(firepower_musuh) * float(rate_of_fire_musuh)/60,2)
combat_effectiveness_musuh =  int (30 *float(firepower_musuh) (40 * (float (rate_of_fire_musuh)**2)/120) +
                                   15 * (float(accuracy_musuh) + float(avasion_musuh)))

#KEPUTUSAN
power_doll = damage_per_second + combat_effectiveness
power_doll_musuh = demage_per_second_musuh + combat_effectiveness_musuh

print ("### RESULT ###")
print (nama_tectical_doll)
print ("demage per second : " + str(damage_per_second))
print ("combat_effectiveness : str(combat_effectiveness)")