def eligma_decrypt(input_string):
    # Jumlahkan angka-angka dalam string
    total = sum(int(char) for char in input_string if char.isdigit())
    
    # Pergeseran alfabet ke kanan sebanyak hasil penjumlahan angka-angka
    shifted_string = ""
    for char in input_string:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + total) % 26 + ascii_offset)
            shifted_string += shifted_char
        else:
            shifted_string += char
    
    # Hapus angka-angka dari string
    output_string = ''.join(char for char in shifted_string if not char.isdigit())
    
    return output_string

# Contoh penggunaan
input_string = "M13b3yni"
output_string = eligma_decrypt(input_string)
print("Output:", output_string)