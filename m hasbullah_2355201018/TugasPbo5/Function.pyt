#                           HS                          #

# Deklarasi Function

# def<function-name>(<Paramters):
#     <body>
# Function-name adalah nama dari fungsi tersebut
# Parameters adalah variabel-variabel yang akan dipakai di dalam function (opsional)
# Body adalah statements yang akan dijalankan ketika function tersebut dipanggil

# Using Function??
# Dengan memanfaatkan function, kita bisa mendapatkan beberapa keuntungan yaitu:
# 1.Program yang dijalankan berkali-kali bisa kita tulis dalam satu kali penulisan
# 2.Merapikan struktur program secara umum
# 3.Lebih mudah untuk dibaca dan dilacak jika terjadi sebuah error

# Calling Function
def selamat():
    print("Selamat, Kamu telah Berhasil!",)
selamat()
selamat()
print('\n')

# Parameter Function
def selamat(nama):
 print("Selamat ulang tahun", nama, "!")
 print("Semoga panjang umur!")

selamat("James")
selamat("Lucy")

# Return Function
# Ketika kita ingin menjalankan beberapa statements yang menghasilkan sebuah nilai, kita bisa membuat function yang akan me-return atau mengembalikan sebuah nilai dan nilainya bisa kita simpan ke dalam sebuah variabel lain. Misalkan kita ingin membuat function tentang perkalian 2 buah integer.
def kali(bil_1, bil_2):
 return bil_1 * bil_2
hasil_1 = kali(2, 3)
hasil_2 = kali(0, 10)
print("Hasil perkalian 2 x 3 adalah " + str(hasil_1))
print("Hasil perkalian 0 x 10 adalah " + str(hasil_2, ),"\n") 

# Return2 Function 
# Using Alternate Mehode!
def kali(bil_1, bil_2):
 return bil_1 * bil_2
print("Hasil perkalian 3 x 5 adalah " + str(kali(3, 5)))

# Apabila kita mencoba mencetak / mengambil nilai dari sebuah function tanpa return value, maka hasilnya adalah None
def selamat_pagi(nama):
 print("Ohayou " + nama)
print(selamat_pagi("Dek Depe"))
# Output:
# Ohayou Dek Depe
# None 
x = selamat_pagi("Dek Depe") #Muncul output: Ohayou Dek Depe
print(x) #Muncul output: None