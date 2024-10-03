def dekripsi(input_str):
    total_pergeseran = sum(int(char) for char in input_str if char.isdigit())  
    hasil = []

    for char in input_str:

        if char.isalpha(): 
            geser = chr((ord(char.lower()) - ord('a') + total_pergeseran) % 26 + ord('a'))
            hasil.append(geser)

    return ''.join(hasil)

input_str = "R3G1NA4"
output = dekripsi(input_str)
print(output)