def hitung_dps(firepower, rate_of_fire):
    dps = (firepower * rate_of_fire) / 60
    return round(dps, 2) 


def combat_effectiveness(firepower, rate_of_fire, accuracy, evasion):
    combat_effectiveness = (
        30 * firepower + 
        40 * (rate_of_fire**2 / 120) +
        15 * (accuracy + evasion)
    )
    return int(combat_effectiveness)


print("Masukkan informasi Tactical Doll milikmu:")
nama_tactical_doll = input("Masukkan nama Tactical Doll: ")
firepower = int(input("Masukkan nilai Firepower: "))
rate_of_fire = int(input("Masukkan nilai Rate of Fire: "))
accuracy = int(input("Masukkan nilai Accuracy: "))
evasion = int(input("Masukkan nilai Evasion: "))



print("\nMasukkan informasi Tactical Doll musuh:")
nama_tactical_doll_musuh = input("Masukkan nama Tactical Doll: ")
firepower_musuh = int(input("Masukkan nilai Firepower: "))
rate_of_fire_musuh = int(input("Masukkan nilai Rate of Fire: "))
accuracy_musuh = int(input("Masukkan nilai Accuracy: "))
evasion_musuh = int(input("Masukkan nilai Evasion: "))


dps = hitung_dps(firepower, rate_of_fire)
ce = combat_effectiveness(firepower, rate_of_fire, accuracy, evasion)


dps_milikmu = hitung_dps(firepower, rate_of_fire)
ce_milikmu = combat_effectiveness(firepower, rate_of_fire, accuracy, evasion)


dps_musuh = hitung_dps(firepower_musuh, rate_of_fire_musuh)
ce_musuh = combat_effectiveness(firepower_musuh, rate_of_fire_musuh, accuracy_musuh, evasion_musuh)


if ce_milikmu > ce_musuh:
    langkah = "MAJUU!!"
else:
    langkah = "KABUR🏃"


nama_lengkap = input("\nMasukkan Nama Lengkap Anda: ")
nim = input("Masukkan NIM Anda: ")


print("\n===== Tactical Doll Challenge Info =====")
print(f"Nama Lengkap Anda: {nama_lengkap}")
print(f"NIM Anda: {nim}")

print("\n===== Tactical Doll Milikmu =====")
print(f"Nama Tactical Doll: {nama_tactical_doll}")
print(f"Damage per Second (DPS): {dps_milikmu}")
print(f"Combat Effectiveness (CE): {ce_milikmu}")

print("\n===== Tactical Doll Musuh =====")
print(f"Nama Tactical Doll: {nama_tactical_doll_musuh}")
print(f"Damage per Second (DPS): {dps_musuh}")
print(f"Combat Effectiveness (CE): {ce_musuh}")

print(f"\nLangkah yang harus diambil: {langkah}")
