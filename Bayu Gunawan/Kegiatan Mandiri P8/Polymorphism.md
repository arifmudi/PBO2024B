# Polymorphism

Polymorphism dalam konteks pemrograman berorientasi objek (OOP) adalah konsep yang memungkinkan satu fungsi atau metode untuk berperilaku berbeda tergantung pada objek yang memanggilnya. Dengan kata lain, polymorphism memungkinkan kita untuk mendefinisikan metode yang memiliki nama yang sama di berbagai kelas, tetapi dengan perilaku yang berbeda tergantung pada objek kelas yang digunakan.

## Jenis Polymorphism

1. Compile-time Polymorphism (Static Polymorphism)

Terjadi saat kompilasi dan biasanya dicapai dengan Method Overloading.

- Method Overloading: Menggunakan nama metode yang sama tetapi dengan jumlah atau jenis parameter yang berbeda.

1. Runtime Polymorphism (Dynamic Polymorphism)

Terjadi saat program dijalankan dan biasanya dicapai dengan Method Overriding.

- Method Overriding: Ketika kelas turunan menggantikan metode yang diwariskan dari kelas induk untuk memberikan implementasi yang lebih spesifik.

## Contoh Method Polymorphism

1.  Method Overriding
    ![polymorphism_overriding.py](polymorphism%20method%20overriding.png)
    Penjelasan Pada Codingan Polymorphism dalam method overriding:

    1. Kelas Animal (Induk)
       - Konstruktor **init**(self, name):
         - Konstruktor ini digunakan untuk menginisialisasi objek dengan nama hewan (name).
         - self.name = name menyimpan nilai nama hewan dalam atribut name.
       - Metode sound(self)
         - Metode ini menghasilkan suara umum untuk objek Animal, misalnya: "{nama} makes a generic sound".
         - Ini adalah metode yang dapat di-override oleh kelas turunan.
    2. Kelas Dog dan Cat (Kelas Turunan):

    - Konstruktor **init**(self, name):Kelas Dog dan Cat mewarisi kelas Animal, artinya mereka memiliki akses ke konstruktor dan metode sound() dari kelas induk.
    - Konstruktor **init**(self, name)
      - Di kelas turunan, super().**init**(name) digunakan untuk memanggil konstruktor dari kelas induk Animal dan menginisialisasi nama hewan.
    - Override metode sound(self)
      - Pada kelas Dog, metode sound() diubah untuk memberikan suara spesifik "Woof!".
      - Pada kelas Cat, metode sound() diubah untuk memberikan suara spesifik "Meow!".

    3. Polymorphism

    - Fungsi animal_sound(animal):
      - Fungsi ini menerima objek animal (baik itu objek Dog atau Cat) dan memanggil metode sound() pada objek tersebut.
      - Meskipun tipe parameter animal adalah Animal, metode sound() yang dipanggil bergantung pada objek yang sesungguhnya (apakah Dog atau Cat).

    4.  Output yang Dikeluarkan

    - Ketika animal_sound(dog) dipanggil, outputnya adalah "Anjing bilang Woof!" karena objek yang diberikan adalah objek Dog.
    - Ketika animal_sound(cat) dipanggil, outputnya adalah "Kucing bilang Meow!" karena objek yang diberikan adalah objek Cat.

2.  Method Overloading
    ![polymorphism_overriding.py](polymorphism%20method%20overloding.png)
    Penjelasan Pada Codingan Polymorphism dalam method overriding:

    1. Konstruktor **init**(self, \*args)
       - \*args memungkinkan kita untuk mengirimkan jumlah parameter yang berbeda ke konstruktor **init** tanpa harus mendefinisikan parameter secara eksplisit.
       - args adalah sebuah tuple yang berisi semua nilai yang diterima saat objek dibuat.
    2. Metode add(self)
       - Metode ini menjumlahkan semua angka yang ada di dalam self.numbers menggunakan fungsi sum().
       - Dengan menggunakan \*args, bisa menambah objek dengan berbagai jumlah angka (1, 2, 3, atau lebih) dan menghitung jumlahnya.
    3. Membuat Objek
       - calc1 = Calculator(5) membuat objek dengan satu angka (5).
       - calc2 = Calculator(5, 3) membuat objek dengan dua angka (5 dan 3).
       - calc3 = Calculator(5, 3, 2) membuat objek dengan tiga angka (5, 3, dan 2). jumlahnya.
    4. Output yang Dikeluarkan
       - calc1.add() mengembalikan 5 karena hanya ada satu angka.
       - calc2.add() mengembalikan 8 karena menjumlahkan 5 dan 3.
       - calc3.add() mengembalikan 10 karena menjumlahkan 5, 3, dan 2.

~supported By~

![alt text](python-3670A0.png)
![alt text](Markdown-000000.png)
