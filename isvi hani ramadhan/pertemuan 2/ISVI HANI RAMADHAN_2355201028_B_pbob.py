class PBOB:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
    
    # Method untuk mendapatkan nama
    def getnama(self):
        return self.nama

    # Method untuk mendapatkan jenis kelamin
    def get_jenis_kelamin(self):
        return self.jenis_kelamin

    # Method untuk mengecek apakah jenis kelamin benar (True) atau tidak (False)
    def cek_jenis_kelamin(self, kelamin_diharapkan):
        if self.jenis_kelamin == kelamin_diharapkan:
            return True
        else:
            return False

# Contoh penggunaan untuk mahasiswa PBO kelas B
mahasiswa = PBOB("vihan", "Laki-Laki")

# Mendapatkan nama dan jenis kelamin
print("Nama:", mahasiswa.getnama()) 
print("Jenis Kelamin:", mahasiswa.get_jenis_kelamin())  

# Mengecek apakah jenis kelamin sesuai dengan yang diharapkan
print(mahasiswa.cek_jenis_kelamin("Laki-Laki")) 
print(mahasiswa.cek_jenis_kelamin("Perempuan")) 
