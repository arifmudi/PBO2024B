class Person:
    def __init__(self, name, gender, ipk):
        self.name = name
        self.gender = gender
        self.ipk = ipk

    def myfunc(self):
        print("Mahasiswa PBO kelas B " + self.name + " mempunyai gender " + self.gender)
        print("dengan IPK " + str(self.ipk))
    
p1 = Person("azhari fajri", "pria", 4.0)
p1.myfunc()