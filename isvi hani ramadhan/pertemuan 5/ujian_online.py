def find_most_similar_question(difficulties):
    # Jika list kosong atau hanya memiliki satu elemen, tidak ada soal lain untuk dibandingkan
    if len(difficulties) < 2:
        return None  # Tidak cukup soal untuk dibandingkan
    
    # Soal bocor adalah elemen pertama
    leaked_difficulty = difficulties[0]
    
    # Variabel untuk menyimpan nilai minimum selisih dan indeks soal paling mirip
    min_difference = float('inf')
    most_similar_index = -1
    
    # Mulai dari soal kedua (index 1) untuk mencari soal mirip
    for i in range(1, len(difficulties)):
        # Hitung selisih tingkat kesulitan
        difference = abs(difficulties[i] - leaked_difficulty)
        
        # Periksa apakah selisih lebih kecil dari yang ditemukan sebelumnya
        if difference < min_difference:
            min_difference = difference
            most_similar_index = i
        # Jika selisih sama, ambil soal dengan nomor lebih kecil
        elif difference == min_difference and i < most_similar_index:
            most_similar_index = i
    
    # Mengembalikan nomor soal yang paling mirip (dalam 1-based index)
    return most_similar_index + 1

# Meminta input dari pengguna
input_difficulties = input("Masukkan tingkat kesulitan soal: ")
# Mengubah input string menjadi list bilangan bulat
difficulties_list = list(map(int, input_difficulties.split()))

# Menjalankan fungsi untuk mencari soal paling mirip
result = find_most_similar_question(difficulties_list)

# Menampilkan hasil
if result:
    print(f"Versi soal paling mirip adalah soal ke: {result}")
else:
    print("Tidak cukup soal untuk dibandingkan.")
