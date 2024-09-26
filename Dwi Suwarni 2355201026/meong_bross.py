def meong_bross():
    # Inisialisasi posisi awal
    x, y = 0, 0
    
    # Input jumlah perintah
    try:
        jumlah_perintah = int(input("Masukkan jumlah perintah: "))
        
        # Validasi input jumlah perintah
        if jumlah_perintah < 0:
            print("Jumlah perintah tidak boleh negatif.")
            return
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")
        return

    # Proses setiap perintah
    for _ in range(jumlah_perintah):
        perintah = input("Masukkan perintah: ").strip()
        
        if perintah == 'U':
            y += 1  # Bergerak ke Utara
        elif perintah == 'S':
            y -= 1  # Bergerak ke Selatan
        elif perintah == 'T':
            x += 1  # Bergerak ke Timur
        elif perintah == 'B':
            x -= 1  # Bergerak ke Barat
        elif perintah == 'HOME':
            break  # Menghentikan eksekusi
        else:
            print("Perintah tidak dikenal, Meong Bross tetap di tempat.")
    
    # Output posisi akhir dengan format yang diminta
    print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")

# Menjalankan program
meong_bross()

