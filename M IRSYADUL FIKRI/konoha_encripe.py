def decrypt_eligma_code(input_string):
    # Inisialisasi variabel untuk menyimpan hasil pergeseran dan total jumlah angka
    total_shift = 0
    result = []

    # Loop melalui setiap karakter dalam input_string
    for char in input_string:
        if char.isdigit():  # Jika karakter adalah angka, tambahkan ke total_shift
            total_shift += int(char)
        elif char.isalpha():  # Jika karakter adalah alfabet, tambahkan ke hasil pergeseran
            result.append(char)

    # Fungsi untuk menggeser alfabet
    def shift_char(c, shift):
        if c.islower():  # Jika karakter huruf kecil
            new_pos = (ord(c) - ord('a') + shift) % 26 + ord('a')
        elif c.isupper():  # Jika karakter huruf besar
            new_pos = (ord(c) - ord('A') + shift) % 26 + ord('A')
        return chr(new_pos)

    # Geser semua huruf di hasil pergeseran sebanyak total_shift
    shifted_result = [shift_char(char, total_shift) for char in result]

    return ''.join(shifted_result)

# Contoh penggunaan program
input_string = input("Masukkan string yang akan didecrypt: ")
output_string = decrypt_eligma_code(input_string)
print("Hasil decrypt:", output_string)

# nama = irsyadul fikri
# nim = 2355201029