Acces Modifikation Python digunakan untuk membatasi akses ke anggota kelas (yaitu, variabel dan metode) dari luar kelas. Tujuan utama access modifier adalah untuk melindungi data dan memastikan kontrol penuh atas bagaimana atribut atau metode diakses atau dimodifikasi.

Tipe Access Modifier
1. Public (public):
Dapat diakses dari mana saja, baik dalam kelas, luar kelas, maupun subclass.
Secara default, semua atribut dan metode di Python adalah public.

2. Protected (protected):
Hanya dapat diakses dalam kelas itu sendiri dan subclass (kelas turunan).
Di Python, ini diimplementasikan dengan menambahkan satu underscore (_) sebelum nama atribut atau metode.

3. Private (private):
Hanya dapat diakses dalam kelas itu sendiri.
Di Python, ini diimplementasikan dengan menambahkan dua underscore (__) sebelum nama atribut atau metode.
Contoh:


KAITAN DENGAN TUGAS 3 : 

1. self.encoded_str (Public)
Deskripsi: Atribut ini menyimpan string terenkripsi yang diberikan sebagai input ke konstruktor.
Access Modifier: Atribut ini bersifat public, sehingga dapat diakses langsung dari luar kelas.
Saran Peningkatan: Jika atribut ini hanya digunakan dalam internal proses kelas, maka sebaiknya dijadikan protected atau private untuk mencegah manipulasi langsung.

self._encoded_str = encoded_str  # Protected

2. self.sum_digits (Public)
Deskripsi: Atribut ini menyimpan total dari semua digit numerik yang terdapat dalam encoded_str.
Access Modifier: Bersifat public, sehingga bisa dimodifikasi dari luar kelas, meskipun ini seharusnya dikelola hanya oleh metode kelas.
Potensi Risiko: Pengguna dapat mengubah nilai atribut ini secara langsung, yang dapat menyebabkan hasil dekripsi menjadi tidak akurat.
Saran Peningkatan: Ganti menjadi private:

self.__sum_digits = 0  # Private

Untuk mendapatkan nilainya, tambahkan getter:

def get_sum_digits(self):
    return self.__sum_digits

3. self.letters (Public)
Deskripsi: Atribut ini menyimpan daftar huruf yang diekstraksi dari encoded_str.
Access Modifier: Bersifat public, sehingga dapat dimodifikasi secara langsung.
Saran Peningkatan: Gunakan private untuk melindunginya:

self.__letters = []


KAITAN DENGAN TUGAS 4 :   

1. self.filename (Public)
Deskripsi: Menyimpan nama file yang akan diproses.
Access Modifier: Bersifat public, sehingga bisa diakses langsung dari luar kelas.
Saran Peningkatan: Jadikan atribut ini protected agar hanya digunakan di dalam kelas atau turunannya:

self._filename = filename  # Protected

2. self.lines (Public)
Deskripsi: Menyimpan daftar baris teks yang dibaca dari file.
Access Modifier: Bersifat public, sehingga bisa dimanipulasi langsung dari luar kelas.
Saran Peningkatan: Jadikan private dan tambahkan getter jika perlu akses dari luar:

self.__lines = []

def get_lines(self):
    return self.__lines

3. self.char_counts (Public)
Deskripsi: Menyimpan jumlah karakter pada setiap baris file.
Access Modifier: Sama seperti self.lines, atribut ini hanya digunakan dalam proses internal.
Saran Peningkatan: Jadikan private:

self.__char_counts = []
self.min_chars, self.max_chars, self.

4. char_range (Public)
Deskripsi: Menyimpan statistik karakter (minimum, maksimum, rentang) dari file.
Access Modifier: Bersifat public, tetapi seharusnya hanya dimanipulasi oleh metode internal.
Saran Peningkatan: Jadikan private:

self.__min_chars = None
self.__max_chars = None
self.__char_range = None

5. read_file (Public)
Deskripsi: Membaca isi file dan menghitung jumlah karakter per baris.
Access Modifier: Bersifat public, tetapi hanya digunakan secara internal dalam kelas.
Saran Peningkatan: Jadikan protected untuk menunjukkan bahwa metode ini tidak untuk diakses dari luar:

def _read_file(self):
    ...


KAITAN DENGAN TUGAS 5 :        

1. Access Modifier dalam Keranjang
Atribut Publik:
  self.nama dan self.kapasitas saat ini bersifat publik, artinya dapat diakses dan diubah langsung dari luar kelas.

keranjang = Keranjang("Buah", 50)
print(keranjang.nama)  # Akses langsung
keranjang.nama = "Sayur"  # Modifikasi langsung

Rekomendasi:
  Jadikan atribut ini privat atau protected menggunakan tanda _ atau __ untuk mencegah akses langsung. Akses dan modifikasi dilakukan melalui getter dan setter.

class Keranjang:
    def __init__(self, nama, kapasitas):
        self.__nama = nama
        self.__kapasitas = kapasitas

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def get_kapasitas(self):
        return self.__kapasitas

    def set_kapasitas(self, kapasitas_baru):
        self.__kapasitas = kapasitas_baru

2. Access Modifier dalam DekDepe
Atribut Internal:
  self.daftar_keranjang saat ini bersifat publik, sehingga data internal dapat diakses dan dimodifikasi secara langsung, yang melanggar prinsip encapsulation.

dek_depe = DekDepe()
dek_depe.daftar_keranjang.append(Keranjang("Buah", 50))  # Tidak aman

Rekomendasi: Ubah menjadi protected dengan _daftar_keranjang.

class DekDepe:
    def __init__(self):
        self._daftar_keranjang = []
