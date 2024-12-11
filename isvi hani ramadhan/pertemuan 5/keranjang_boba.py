daftar_keranjang = []

def beli_keranjang(nama_keranjang, kapasitas_keranjang):
    '''
    Implementasikan fungsi untuk menambahkan
    keranjang dengan nama 'nama_keranjang'
    dan kapasitas 'kapasitas_keranjang'
    '''
    daftar_keranjang.append([nama_keranjang, kapasitas_keranjang])
    print(f"Berhasil menambahkan {nama_keranjang} dengan kapasitas {kapasitas_keranjang}")

def jual_keranjang(indeks):
    '''
    Implementasikan fungsi untuk menghapus
    keranjang dengan index 'indeks'
    '''
    if 0 <= indeks < len(daftar_keranjang):
        keranjang = daftar_keranjang.pop(indeks)
        print(f"Berhasil menjual {keranjang[0]} yang memiliki kapasitas sebesar {keranjang[1]}")
    else:
        print("Indeks tidak valid")

def ubah_kapasitas(indeks, kapasitas_baru):
    '''
    Implementasikan fungsi untuk mengubah kapasitas
    keranjang dengan index 'indeks' menjadi 'kapasitas_baru'
    '''
    if 0 <= indeks < len(daftar_keranjang):
        daftar_keranjang[indeks][1] = kapasitas_baru
        print(f"Berhasil mengubah kapasitas {daftar_keranjang[indeks][0]} menjadi {kapasitas_baru}")
    else:
        print("Indeks tidak valid")

def ubah_nama(indeks, nama_baru):
    '''
    Implementasikan fungsi untuk mengubah nama
    keranjang dengan index 'indeks' menjadi 'nama_baru'
    '''
    if 0 <= indeks < len(daftar_keranjang):
        nama_lama = daftar_keranjang[indeks][0]
        daftar_keranjang[indeks][0] = nama_baru
        print(f"Berhasil mengubah nama {nama_lama} menjadi {nama_baru}")
    else:
        print("Indeks tidak valid")

def lihat(indeks):
    '''
    Implementasikan fungsi untuk mencetak informasi
    keranjang dengan index 'indeks'
    '''
    if 0 <= indeks < len(daftar_keranjang):
        nama, kapasitas = daftar_keranjang[indeks]
        print(f"Keranjang {nama} memiliki kapasitas sebesar {kapasitas}")
    else:
        print("Indeks tidak valid")

def lihat_semua():
    '''
    Implementasikan fungsi untuk mencetak semua 
    keranjang dalam bentuk table
    '''
    print("Keranjang Dek Depe")
    print("-" * 30)
    for nama, kapasitas in daftar_keranjang:
        print(f"{nama:<20} | {kapasitas}")

def total_kapasitas():
    '''
    Implementasikan fungsi yang mereturn
    sebuah integer yang menyatakan
    total kapasitas keranjang yang dimiliki Dek Depe
    '''
    total = sum(k[1] for k in daftar_keranjang)
    print(f"Total kapasitas keranjang Dek Depe adalah {total}")


'''
Baris-baris program di bawah ini adalah main program dari program ini.
'''
jumlah_operasi = int(input("Masukkan banyak operasi: "))
for i in range(jumlah_operasi):
    operasi = input(f"Operasi {i+1}: ")  # Input query sebagai 1 string
    
    # Pecah operasi menggunakan method .split() dan tampung ke sebuah variable
    parts = operasi.split()
    op = parts[0]

    if op == "beli":
        nama_keranjang = parts[1]
        kapasitas_keranjang = int(parts[2])
        beli_keranjang(nama_keranjang, kapasitas_keranjang)
    elif op == "jual":
        indeks = int(parts[1])
        jual_keranjang(indeks)
    elif op == "ubah_kapasitas":
        indeks = int(parts[1])
        kapasitas_baru = int(parts[2])
        ubah_kapasitas(indeks, kapasitas_baru)
    elif op == "ubah_nama":
        indeks = int(parts[1])
        nama_baru = parts[2]
        ubah_nama(indeks, nama_baru)
    elif op == "lihat":
        indeks = int(parts[1])
        lihat(indeks)
    elif op == "lihat_semua":
        lihat_semua()
    elif op == "total_kapasitas":
        total_kapasitas()
    else:
        print("masukkan banyak operasi")
