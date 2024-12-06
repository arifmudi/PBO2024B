class CharacterCounter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.char_counts = []
        self.lines = []

    def read_file(self):
        """Membaca isi file dan menyimpan jumlah karakter per baris."""
        try:
            with open(self.file_name, "r") as in_file:
                self.lines = in_file.readlines()
            
            if not self.lines:
                # Jika file kosong, tulis 'NULL' dan beri informasi
                self.write_null()
                return False

            # Menghitung jumlah karakter per baris (menghapus newline)
            self.char_counts = [len(line.rstrip('\n')) for line in self.lines]
            return True
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' tidak ditemukan.")
        except PermissionError:
            print(f"Error: Tidak memiliki izin untuk mengakses file '{self.file_name}'.")
        except IOError as e:
            print(f"Error: Terjadi masalah saat membaca file '{self.file_name}'. ({e})")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}")
        return False

    def write_null(self):
        """Menulis 'NULL' ke dalam file jika file kosong."""
        try:
            with open(self.file_name, "w") as out_file:
                out_file.write("NULL")
            print(f"File kosong. Output 'NULL' ditulis ke {self.file_name}.")
        except PermissionError:
            print(f"Error: Tidak dapat menulis ke file '{self.file_name}'. Pastikan file dapat ditulis.")
        except IOError as e:
            print(f"Error: Terjadi masalah saat menulis ke file '{self.file_name}'. ({e})")

    def calculate_stats(self):
        """Menghitung statistik karakter: min, max, dan range."""
        try:
            if not self.char_counts:
                raise ValueError("Tidak ada data karakter untuk dihitung.")
            min_chars = min(self.char_counts)
            max_chars = max(self.char_counts)
            range_chars = max_chars - min_chars
            return min_chars, max_chars, range_chars
        except ValueError as e:
            print(f"Error: {e}")
            return None, None, None

    def write_output(self):
        """Menulis output statistik ke dalam file baru."""
        min_chars, max_chars, range_chars = self.calculate_stats()
        
        # Hanya menulis output jika statistik valid
        if min_chars is None or max_chars is None or range_chars is None:
            print("Tidak dapat menulis statistik karena kesalahan perhitungan.")
            return

        try:
            # Membuat nama file output untuk menulis hasil
            output_file = f"output_{self.file_name}"
            with open(output_file, "w") as out_file:
                out_file.write("".join(self.lines))  # Menambahkan isi file sebelumnya
                out_file.write("\n... Isi dari berkas " + self.file_name + " sebelumnya ...\n")
                out_file.write("###########\n")
                out_file.write(f"Min: {min_chars} karakter\n")
                out_file.write(f"Max: {max_chars} karakter\n")
                out_file.write(f"Range: {range_chars} karakter\n")
            print(f"Output statistik berhasil ditulis ke {output_file}")
        except PermissionError:
            print(f"Error: Tidak dapat menulis ke file '{output_file}'. Pastikan file dapat ditulis.")
        except IOError as e:
            print(f"Error: Terjadi masalah saat menulis ke file '{output_file}'. ({e})")

def main():
    # Meminta nama file input dari user
    file_name = input("Masukkan nama file input: ")
    counter = CharacterCounter(file_name)

    if counter.read_file():
        counter.write_output()
    else:
        print("Proses gagal. Pastikan file ada dan bisa dibaca.")
    
    input("Program selesai. Tekan enter untuk keluar...")

if __name__ == "__main__":
    main()
