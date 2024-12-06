Pewarisan Python

Pewarisan memungkinkan kita mendefinisikan kelas yang mewarisi semua metode dan properti dari kelas lain.

Kelas induk adalah kelas yang diwarisi, disebut juga kelas dasar.

Kelas anak adalah kelas yang mewarisi dari kelas lain, disebut juga kelas turunan.

Buat Kelas Induk
Kelas apa pun bisa menjadi kelas induk, jadi sintaksnya sama dengan membuat kelas lainnya:

Contoh :
Buat kelas bernama Person, dengan properti dan firstnamemetode :lastnameprintname

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

Buat Kelas Anak
Untuk membuat kelas yang mewarisi fungsionalitas dari kelas lain, kirimkan kelas induk sebagai parameter saat membuat kelas anak:

Contoh
Buat kelas bernama Student, yang akan mewarisi properti dan metode dari Personkelas:

class Student(Person):
  pass

Sekarang kelas Student memiliki properti dan metode yang sama dengan kelas Person.

Contoh
Gunakan Studentkelas untuk membuat objek, lalu jalankan printnamemetode:

x = Student("Mike", "Olsen")
x.printname()


Tambahkan Fungsi __init__()
Sejauh ini kita telah membuat kelas anak yang mewarisi properti dan metode dari induknya.

Menambahkan __init__()fungsi ke kelas anak (bukan passkata kunci).

Catatan: Fungsi ini __init__()dipanggil secara otomatis setiap kali kelas digunakan untuk membuat objek baru.

Contoh
Tambahkan __init__()fungsi ke Studentkelas:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

Ketika Anda menambahkan __init__()fungsi tersebut, kelas anak tidak akan lagi mewarisi fungsi induknya __init__().

Untuk mempertahankan pewarisan __init__() fungsi induk, tambahkan panggilan ke fungsi induk __init__():

Contoh
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

Sekarang kita telah berhasil menambahkan __init__()fungsi tersebut, dan mempertahankan warisan kelas induk, dan kita siap untuk menambahkan fungsionalitas ke dalam __init__()fungsi tersebut.


Gunakan Fungsi super()
Python juga memiliki super()fungsi yang akan membuat kelas anak mewarisi semua metode dan properti dari induknya:

Contoh
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


Contoh CODE python :
Contoh Kode dengan Inheritance
python
Salin kode
# Kelas induk
class Electronics:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} sedang dinyalakan.")

# Kelas anak: Phone
class Phone(Electronics):
    def make_call(self, number):
        print(f"Telepon {self.brand} sedang menelepon {number}.")

# Kelas anak: Laptop
class Laptop(Electronics):
    def open_software(self, software):
        print(f"{self.brand} sedang membuka perangkat lunak {software}.")

# Contoh penggunaan
phone = Phone("Samsung")
laptop = Laptop("Dell")

phone.power_on()           # Memanggil metode dari kelas induk
phone.make_call("08123456789")  # Metode spesifik kelas Phone

laptop.power_on()          # Memanggil metode dari kelas induk
laptop.open_software("Python")  # Metode spesifik kelas Laptop