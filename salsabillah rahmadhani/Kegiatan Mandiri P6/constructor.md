Konstruktor dalam Object-Oriented Programming (OOP) adalah metode khusus yang digunakan untuk menginisialisasi objek dari sebuah kelas. Konstruktor dipanggil secara otomatis ketika sebuah objek baru dari kelas dibuat. Fungsi utama dari konstruktor adalah untuk menginisialisasi atribut-atribut objek tersebut sehingga objek siap digunakan.

KAITAN DENGAN TUGAS 3 :

Konstruktor dalam kelas Konoha adalah metode __init__. Konstruktor ini bertanggung jawab untuk menginisialisasi atribut-atribut yang diperlukan oleh objek yang dibuat dari kelas tersebut.

Fungsi Konstruktor dalam Kode

class Konoha:
    def __init__(self, encoded_str):
        self.encoded_str = encoded_str
        self.sum_digits = 0
        self.letters = []

1. Parameter encoded_str:
Konstruktor menerima parameter encoded_str, yaitu string yang berisi kombinasi huruf dan angka yang akan diproses.
Nilai ini diberikan saat objek dibuat (contohnya, decoder = Konoha(input_str)).
2. Inisialisasi Atribut:
self.encoded_str: Menyimpan string yang akan diproses, sehingga metode lain di kelas dapat mengaksesnya.
self.sum_digits: Diinisialisasi dengan nilai 0, digunakan untuk menyimpan jumlah digit yang ditemukan dalam string.
self.letters: Diinisialisasi sebagai daftar kosong, digunakan untuk mengumpulkan huruf dari string.


KAITAN DENGAN TUGAS 4 :

Pada kelas IOException, konstruktor (__init__) memainkan peran yang sangat penting untuk menginisialisasi atribut dan langsung menjalankan logika pemrosesan file. 

