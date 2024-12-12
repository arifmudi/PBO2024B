class Konoha:
    def __init__(self, encoded_str):
        self.encoded_str = encoded_str
        self.sum_digits = 0 
        self.letters = []

    def calculate_sum_of_digits(self):
        """Menghitung jumlah angka dalam string."""
        for char in self.encoded_str:
            if char.isdigit():
                self.sum_digits += int(char)

    def collect_letters(self):
        """Mengumpulkan huruf dari string."""
        for char in self.encoded_str:
            if char.isalpha():
                self.letters.append(char)

    def decrypt(self):
        """Melakukan dekripsi string berdasarkan jumlah angka yang dihitung."""
        self.calculate_sum_of_digits()


        if self.sum_digits == 0:
            print("Tidak memiliki angka")
            return ""

        self.collect_letters()


        shift = self.sum_digits % 26  


        decrypted_letters = []

        for letter in self.letters:
            if letter.islower():
                # Geser huruf kecil
                new_char = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
            else:
                # Geser huruf besar
                new_char = chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
            decrypted_letters.append(new_char)

        return ''.join(decrypted_letters)

# Contoh penggunaan
input_str = "aaaa1"
decoder = Konoha(input_str)
output = decoder.decrypt()
print(output)