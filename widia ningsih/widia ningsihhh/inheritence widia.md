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

Dengan menggunakan super()fungsi tersebut, tidak perlu menggunakan nama elemen induk, maka secara otomatis akan mewarisi metode dan properti dari induknya.


Tambahkan Properti
Contoh
Tambahkan properti yang disebut graduationyearke Studentkelas:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

Dalam contoh di bawah ini, tahun 2019harus berupa variabel, dan dimasukkan ke dalam Studentkelas saat membuat objek siswa. Untuk melakukannya, tambahkan parameter lain dalam __init__()fungsi:

Contoh
Tambahkan yearparameter, dan masukkan tahun yang benar saat membuat objek:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


Tambahkan Metode
Contoh
Tambahkan metode yang dipanggil welcomeke Studentkelas:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
Jika Anda menambahkan metode di kelas anak dengan nama yang sama dengan fungsi di kelas induk, pewarisan metode induk akan ditimpa.


CONTOH :
Kelas induk Animal, yang memiliki properti umum seperti nama dan metode umum seperti speak.
Kelas anak Dog dan Cat, yang mewarisi dari Animal tetapi memiliki metode spesifik mereka sendiri.
Contoh Kode dengan Inheritance

# Kelas induk
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} membuat suara.")

# Kelas anak: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Memanggil konstruktor kelas induk
        self.breed = breed  # Properti tambahan khusus Dog

    def speak(self):
        # Override metode speak untuk Dog
        print(f"{self.name}, seekor {self.breed}, menggonggong: 'Woof woof!'")

# Kelas anak: Cat
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Memanggil konstruktor kelas induk
        self.color = color  # Properti tambahan khusus Cat

    def speak(self):
        # Override metode speak untuk Cat
        print(f"{self.name}, seekor kucing berwarna {self.color}, mengeong: 'Meow!'")

# Contoh penggunaan
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Mittens", "Putih")

dog.speak()  # Memanggil versi metode di kelas Dog
cat.speak()  # Memanggil versi metode di kelas Cat
Penjelasan Kode
Kelas Induk: Animal

Konstruktor __init__ menerima properti umum seperti name.
Metode speak mencetak pesan umum untuk hewan.
Kelas Anak: Dog

Menambahkan properti breed (ras).
Meng-override metode speak untuk memberikan pesan spesifik untuk anjing.
Kelas Anak: Cat

Menambahkan properti color (warna).
Meng-override metode speak untuk memberikan pesan spesifik untuk kucing.
Pewarisan

Kedua kelas anak mewarisi properti dan metode dari Animal tetapi juga menambahkan fitur khusus mereka sendiri.
Output
Jika kode di atas dijalankan, hasilnya seperti ini:

Buddy, seekor Golden Retriever, menggonggong: 'Woof woof!'
Mittens, seekor kucing berwarna Putih, mengeong: 'Meow!'
