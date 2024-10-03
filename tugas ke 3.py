def decrypt_eligma_code(input_string):
    # Memisahkan angka dan huruf dari string input
    letters = []
    total_shift = 0
    
    for char in input_string:
        if char.isdigit():
            total_shift += int(char)  # Menambahkan angka ke total_shift
        else:
            letters.append(char)  # Memasukkan huruf ke list letters
    
    # Menggeser setiap huruf sesuai total_shift
    decrypted_string = ""
    for letter in letters:
        # Menghitung posisi baru untuk huruf, dengan wrapping jika melebihi 'z'
        new_char = chr(((ord(letter) - ord('a') + total_shift) % 26) + ord('a'))
        decrypted_string += new_char
    
    return decrypted_string

# Contoh penggunaan
input_string = "M13b3yni"
# Konversi input menjadi lowercase karena alfabetnya dioperasikan pada huruf kecil
output = decrypt_eligma_code(input_string.lower())
print(output) 