Atribut dalam Object-Oriented Programming (OOP) adalah variabel yang terkait dengan class atau object. Atribut ini menyimpan data atau informasi yang dimiliki oleh objek. Atribut bisa didefinisikan dalam konstruktor atau di dalam metode class, dan mereka merepresentasikan karakteristik atau properti dari objek tersebut.


KAITAN DENGAN TUGAS 5 :

class Keranjang:
    def __init__(self, nama, kapasitas):
        self.nama = nama  # Atribut Instance
        self.kapasitas = kapasitas  # Atribut Instance

class DekDepe:
    def __init__(self):
        self.daftar_keranjang = []  # Atribut Instance

    def beli(self, nama, kapasitas):
        """Menambahkan keranjang baru ke daftar."""
        self.daftar_keranjang.append(Keranjang(nama, kapasitas))
        print(f"Berhasil menambahkan {nama} dengan kapasitas {kapasitas}")



KAITAN DENGAN TUGAS 4:

Penjelasan Atribut pada Kode:
1. self.filename:
Ini adalah atribut instance yang menyimpan nama file yang diberikan saat objek IOException dibuat. Atribut ini diinisialisasi melalui parameter yang diterima oleh konstruktor __init__(). Nama file ini digunakan untuk membuka dan membaca isi file.
2. self.lines:
Atribut ini menyimpan daftar (list) yang berisi setiap baris dari file yang dibaca. Dalam metode read_file(), setiap baris file dibaca dan disimpan dalam atribut lines.
Contoh pengisian: self.lines = in_file.readlines(), yang membaca seluruh baris file ke dalam list.
3. self.char_counts:
Atribut ini menyimpan daftar (list) yang berisi jumlah karakter pada setiap baris file. Penghitungannya dilakukan dengan menghitung panjang setiap baris yang telah dibaca dan dihapus karakter baris baru (\n).
Contoh pengisian: self.char_counts = [len(line.rstrip('\n')) for line in self.lines].
4. self.min_chars:
Atribut ini digunakan untuk menyimpan jumlah karakter terkecil dari semua baris dalam file setelah penghitungan dilakukan di metode calculate_stats(). Atribut ini diisi dengan hasil dari fungsi min(self.char_counts).
5. self.max_chars:
Atribut ini digunakan untuk menyimpan jumlah karakter terbesar dari semua baris dalam file setelah penghitungan dilakukan di metode calculate_stats(). Atribut ini diisi dengan hasil dari fungsi max(self.char_counts).
6. self.char_range:
Atribut ini menyimpan rentang jumlah karakter antara baris dengan jumlah karakter terbanyak dan yang paling sedikit. Rentang dihitung dengan selisih antara self.max_chars dan self.min_chars.


KAITAN DENGAN TUGAS 3 :

Penjelasan Atribut:
1. self.encoded_str:
- Atribut ini menyimpan string yang terkodekan (encoded string) yang akan diproses. Nilai dari atribut ini diberikan saat objek Konoha dibuat dan diproses lebih lanjut dalam metode lain, seperti calculate_sum_of_digits() dan collect_letters().
- Contoh penggunaan: Pada baris decoder = Konoha(input_str), input_str diassign ke atribut self.encoded_str untuk diproses lebih lanjut dalam class Konoha.
2. self.sum_digits:
- Atribut ini digunakan untuk menyimpan jumlah total dari digit yang ada di dalam string encoded_str. Atribut ini akan dihitung dalam metode calculate_sum_of_digits(). Pada awalnya, atribut ini diinisialisasi dengan nilai 0, dan setiap kali ada digit ditemukan dalam string, nilai atribut ini akan ditambahkan.
- Contoh penggunaan: Dalam metode calculate_sum_of_digits(), setiap digit dalam self.encoded_str yang ditemukan akan dijumlahkan ke dalam self.sum_digits.
3. self.letters:
- Atribut ini menyimpan daftar (list) dari huruf-huruf yang ada dalam encoded_str. Atribut ini diisi dengan huruf-huruf yang dipisahkan dari digit dalam string. Huruf-huruf ini akan digunakan untuk proses dekripsi dalam metode decrypt().
- Contoh penggunaan: Dalam metode collect_letters(), huruf-huruf yang ditemukan dalam string self.encoded_str akan dimasukkan ke dalam list self.letters.
