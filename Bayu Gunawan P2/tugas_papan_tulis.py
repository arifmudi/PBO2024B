# ~             CF2                         ~ 
# 1. Class And Object in The_init_("Function")

class PBOB:
    def __init__(deklarasi, nama, jenis_kelamin):
        deklarasi.nama = nama
        deklarasi.jenis_kelamin = jenis_kelamin

CF = PBOB("Bayu Gunawan", "Laki-Laki")

print (CF.nama)
print (CF.jenis_kelamin)

print("*OR*")

print ("Nama " + CF.nama)
print ("Jenis Kelamin " + CF.jenis_kelamin)

# 2.Alternate
class mahasiswa :
    def __init__(deklarasi, nama, jenis_kelamin, mahasiswa):
        deklarasi.nama = nama
        deklarasi.jenis_kelamin = jenis_kelamin
        deklarasi.mahasiswa = mahasiswa

    def info(deklarasi):
        status_mahasiswa = "Mahasiswa PBO Kelas B" if deklarasi.mahasiswa else "Mahasiswa PBO Kelas A"
        return f"Nama saya adalah {deklarasi.nama} dan Jenis Kelamin saya {deklarasi.jenis_kelamin} status {status_mahasiswa}"

mahasiswa1 = mahasiswa("Bayu Gunawan", "Laki-Laki", True)
mahasiswa2 = mahasiswa("Alice In Wonderland", "Perempuan", False)

print (mahasiswa1.info())
print (mahasiswa2.info())