def meong_bross():
    # Posisi awal Meongbross
    x, y = 0, 0
    jalur = [(x, y)]
    
    # Input jumlah perintah
    try :
        jumlah_perintah = int(input("Masukkan jumlah perintah: "))
        
        # Identifikasi input jumlah perintah
        if jumlah_perintah < 0:
            print("Jumlah perintah adalah bilangan tidak negatif.")
            
    except ValueError:
        print("no valid. Coba masukkan bilangan bulat!")
        

    # Proses setiap perintah
    for _ in range(jumlah_perintah):
        p = input("Masukkan perintah: ").strip()
        
        if p == 'U':
            y += 1  # Bergerak ke Utara
        elif p == 'S':
            y -= 1  # Bergerak ke Selatan
        elif p == 'T':
            x += 1  # Bergerak ke Timur
        elif p == 'B':
            x -= 1  # Bergerak ke Barat
        elif p == 'HOME':
            break  # Menghentikan eksekusi
        else:
            print("GAGAL, Meong Bross tidak bergerak.")
            
        # Tambahkan posisi baru ke jalur
        jalur.append((x, y))
    
    # Format output
    jalur_output = "-".join(f"({x},{y})" for x, y in jalur)
    print(f"Jalur yang ditempuh meong bross adalah {jalur_output}")

# Panggil fungsi
meong_bross()