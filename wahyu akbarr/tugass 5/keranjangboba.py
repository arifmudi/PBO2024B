class Keranjang:
    def __init__(self, nama, kapasitas, jenis):
        self.nama = nama
        self.kapasitas = kapasitas
        self.jenis = jenis  # Jenis barang, misalnya "Ayam", "Teh", dll.

class DekDepe:
    def __init__(self):
        self.daftar_keranjang = []

    def beli(self, nama, kapasitas, jenis):
        """Menambahkan keranjang baru ke daftar."""
        self.daftar_keranjang.append(Keranjang(nama, kapasitas, jenis))
        print(f"Berhasil menambahkan {nama} ({jenis}) dengan kapasitas {kapasitas}")

    def jual(self, indeks):
        """Menghapus keranjang dari daftar berdasarkan indeks."""
        if 0 <= indeks < len(self.daftar_keranjang):
            keranjang = self.daftar_keranjang.pop(indeks)
            print(f"Berhasil menjual {keranjang.nama} ({keranjang.jenis}) yang memiliki kapasitas sebesar {keranjang.kapasitas}")
        else:
            print("Indeks tidak valid")

    def ubah_kapasitas(self, indeks, kapasitas_baru):
        """Mengubah kapasitas keranjang berdasarkan indeks."""
        if 0 <= indeks < len(self.daftar_keranjang):
            self.daftar_keranjang[indeks].kapasitas = kapasitas_baru
            print(f"Berhasil mengubah kapasitas {self.daftar_keranjang[indeks].nama} menjadi {kapasitas_baru}")
        else:
            print("Indeks tidak valid")

    def ubah_nama(self, indeks, nama_baru):
        """Mengubah nama keranjang berdasarkan indeks."""
        if 0 <= indeks < len(self.daftar_keranjang):
            self.daftar_keranjang[indeks].nama = nama_baru
            print(f"Berhasil mengubah nama menjadi {nama_baru}")
        else:
            print("Indeks tidak valid")

    def lihat(self, indeks):
        """Melihat informasi keranjang berdasarkan indeks."""
        if 0 <= indeks < len(self.daftar_keranjang):
            keranjang = self.daftar_keranjang[indeks]
            print(f"Keranjang {keranjang.nama} ({keranjang.jenis}) memiliki kapasitas sebesar {keranjang.kapasitas}")
        else:
            print("Indeks tidak valid")

    def lihat_semua(self):
        """Menampilkan semua keranjang dalam format tabel."""
        print("Keranjang Dek Depe")
        print("---------------------------")
        print(f"{'Nama':<20} | {'Jenis':<10} | {'Kapasitas':<10}")
        print("---------------------------")
        for keranjang in self.daftar_keranjang:
            print(f"{keranjang.nama:<20} | {keranjang.jenis:<10} | {keranjang.kapasitas:<10}")

    def total_kapasitas(self):
        """Menghitung total kapasitas berdasarkan jenis barang."""
        jenis_total = {}
        for keranjang in self.daftar_keranjang:
            if keranjang.jenis not in jenis_total:
                jenis_total[keranjang.jenis] = 0
            jenis_total[keranjang.jenis] += keranjang.kapasitas

        print("Total kapasitas berdasarkan jenis barang:")
        for jenis, total in jenis_total.items():
            print(f"Total kapasitas untuk {jenis}: {total}")

def validasi_input_integer(prompt, error_message="Input tidak valid! Harap masukkan angka yang benar."):
    """Fungsi untuk validasi input integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)

def main():
    dek_depe = DekDepe()
    n = validasi_input_integer("Masukkan banyak operasi: ")

    for i in range(n):
        operasi = input(f"Operasi {i+1}: ").split()
        if operasi[0] == "BELI":
            nama = operasi[1]
            jenis = operasi[2]
            kapasitas = validasi_input_integer(f"Masukkan kapasitas untuk {nama} ({jenis}): ")
            dek_depe.beli(nama, kapasitas, jenis)
        elif operasi[0] == "JUAL":
            indeks = validasi_input_integer(f"Masukkan indeks keranjang yang ingin dijual: ")
            dek_depe.jual(indeks)
        elif operasi[0] == "UBAH_KAPASITAS":
            indeks = validasi_input_integer(f"Masukkan indeks keranjang yang ingin diubah kapasitasnya: ")
            kapasitas_baru = validasi_input_integer("Masukkan kapasitas baru: ")
            dek_depe.ubah_kapasitas(indeks, kapasitas_baru)
        elif operasi[0] == "UBAH_NAMA":
            indeks = validasi_input_integer(f"Masukkan indeks keranjang yang ingin diubah namanya: ")
            nama_baru = operasi[2]
            dek_depe.ubah_nama(indeks, nama_baru)
        elif operasi[0] == "LIHAT":
            indeks = validasi_input_integer(f"Masukkan indeks keranjang yang ingin dilihat: ")
            dek_depe.lihat(indeks)
        elif operasi[0] == "LIHAT_SEMUA":
            dek_depe.lihat_semua()
        elif operasi[0] == "TOTAL_KAPASITAS":
            dek_depe.total_kapasitas()

if __name__ == "__main__":
    main()
