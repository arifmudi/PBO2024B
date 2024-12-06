# meong_bross.py

# Fungsi untuk menghitung posisi akhir Meong Bross
def hitung_koordinat(banyak_perintah):
    # Koordinat awal (0, 0)
    x, y = 0, 0

    # Loop untuk memproses setiap perintah
    for _ in range(banyak_perintah):
        perintah = input("Masukkan perintah : ")
        
        # Memproses perintah sesuai dengan arah
        if perintah == "U":
            y += 1  # Bergerak ke Utara (Y positif)
        elif perintah == "S":
            y -= 1  # Bergerak ke Selatan (Y negatif)
        elif perintah == "T":
            x += 1  # Bergerak ke Timur (X positif)
        elif perintah == "B":
            x -= 1  # Bergerak ke Barat (X negatif)
        elif perintah == "HOME":
            x, y = 0, 0  # Kembali ke titik asal
        else:
            continue  # Abaikan input lain (tetap di posisi)

    # Mengembalikan koordinat akhir
    return x, y

# Fungsi utama
def main():
    # Input banyak perintah
    banyak_perintah = int(input("Banyak perintah : "))

    # Jika banyak perintah adalah 0, langsung output posisi awal
    if banyak_perintah == 0:
        print("Karakter Meong Brosss berada di koordinat (0,0)")
    else:
        # Hitung koordinat akhir
        x_akhir, y_akhir = hitung_koordinat(banyak_perintah)
        
        # Output koordinat akhir
        print(f"Karakter Meong Brosss berada di koordinat ({x_akhir},{y_akhir})")

# Menjalankan program utama
if __name__ == "__main__":
    main()
