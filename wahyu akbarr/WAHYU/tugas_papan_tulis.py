# ~             CF2                         ~ 
# 1. Class And Object in The_init_("Function")

class PBOB:
    def __init__(deklarasi, nama, jenis_kelamin):
        deklarasi.nama = nama
        deklarasi.jenis_kelamin = jenis_kelamin

NAMA = PBOB("WAHYU AKBAR HABIBI", "Laki-Laki")

print (NAMA.nama)
print (NAMA.jenis_kelamin)

print("*OR*")

print ("Nama " + NAMA.nama)
print ("Jenis Kelamin " + NAMA.jenis_kelamin)

# 2.Alternate
class mahasiswa :
    def __init__(deklarasi, nama, jenis_kelamin, mahasiswa):
        deklarasi.nama = nama
        deklarasi.jenis_kelamin = jenis_kelamin
        deklarasi.mahasiswa = mahasiswa

    def info(deklarasi):
        status_mahasiswa = "Mahasiswa INFORMATIKA PBO Kelas B" if deklarasi.mahasiswa else "Mahasiswa INFORMATIKA PBO Kelas B"
        return f"Nama saya adalah {deklarasi.nama} dan Jenis Kelamin saya {deklarasi.jenis_kelamin} status {status_mahasiswa}"

mahasiswa1 = mahasiswa("WAHYU AKBAR HABIBI", "Laki-Laki", True)
mahasiswa2 = mahasiswa("KEISA", "Perempuan", False)

print (mahasiswa1.info())
print (mahasiswa2.info())