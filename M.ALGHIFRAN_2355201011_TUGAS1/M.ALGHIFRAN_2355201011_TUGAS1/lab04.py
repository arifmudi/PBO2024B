#                           CF2                                     #
def main():
    # Menerima input nama file
    filename = input("Masukkan nama file: ")

    try:
        # Membuka file untuk dibaca
        with open(filename, "r") as in_file:
            lines = in_file.readlines()

        # Jika file kosong, tulis NULL dan keluar
        if not lines:
            with open(filename, "w") as out_file:
                out_file.write("NULL\n")
            print('NULL')
            return

        # Menghitung jumlah karakter per baris
        # count untuk mengghitung karakter pada baris
        char_counts = [len(line) for line in lines]  # Hitung karakter per baris

        # Mencari nilai min, max dan rentang
        min_chars = min(char_counts)
        max_chars = max(char_counts)
        char_range = max_chars - min_chars

        # Menampilkan hasil ke layar
        print(f"Min: {min_chars} karakter")
        print(f"Max: {max_chars} karakter")
        print(f"Range: {char_range} karakter")

        # Menyimpan hasil ke dalam file
        with open(filename, "a") as out_file:
            out_file.write("######## \n")
            out_file.write(f"Min: {min_chars} karakter\n")
            out_file.write(f"Max: {max_chars} karakter\n")
            out_file.write(f"Range: {char_range} karakter\n")

    except FileNotFoundError:
        print("Error: File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
