
def hitung_dps(firepower, rate_or_fire):
    return round(firepower * rate_of_fire / 60, 2)
#menghitung combat effectiveness
def hitung_combat_effectiveness(firepower, accuracy, rat_of_fire, evasion):
    return firepower + accucary + rate_of_fire + evasion

nama_tactical_doll = input("Masukkan nama Tactical Doll: ")
firepower = int(input("Masukkan nilai Firepower: "))
accucary = int(input("Masukkan nilai Accucary: "))
rate_of_fire = int(input("Masukkan nilai Rate of Fire: "))
evasion = int(input("Masukkan nilai Evasion: "))

dps = hitung_dps(firepower, rate_of_fire)
combat_effectiveness = hitung_combat_effectiveness(firepower, accucary, rate_of_fire, evasion)

print(f"\nNama Tactical Doll:{nama_tactical_doll}")
print(f"Damage per Second (DPS): {dps}")
print(f"Combat Effectiveness:{int(combat_effectiveness)}")