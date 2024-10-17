def prediksi_koordinat_meong_bross():
    # Inisialisasi posisi awal Meong Bross di koordinat (0, 0)
    x, y = 0, 0
    
    # Meminta input jumlah perintah
    try:
        banyak_perintah = int(input("Masukkan banyak perintah: "))
    except ValueError:
        print("Input harus berupa bilangan bulat non negatif.")
        return
    
    # Memastikan jumlah perintah adalah non-negatif
    if banyak_perintah < 0:
        print("Jumlah perintah tidak bisa negatif.")
        return
    
    # Loop untuk menerima perintah sebanyak yang dimasukkan
    for i in range(banyak_perintah):
        perintah = input(f"Masukkan perintah ke-{i+1}: ")

        # Cek perintah dan sesuaikan pergerakan Meong Bross
        if perintah == "U":
            y += 1  # Bergerak ke Utara
        elif perintah == "S":
            y -= 1  # Bergerak ke Selatan
        elif perintah == "T":
            x += 1  # Bergerak ke Timur
        elif perintah == "B":
            x -= 1  # Bergerak ke Barat
        elif perintah == "HOME":
            x, y = 0, 0  # Kembali ke titik pusat (0, 0)
        else:
            # Jika perintah tidak valid, Meong Bross tetap di tempat
            continue

    # Output hasil akhir
    print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")

# Menjalankan program
prediksi_koordinat_meong_bross()
