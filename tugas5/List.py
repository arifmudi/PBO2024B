#                           fk                                 #

# Deklarasi List
list1 = []
list2 = [1, 2, 3]
list3 = [1, "Hello", [1, 2, 3]]

print (list1)
print (list2)
print (list3, "\n")

# Constructor() List
list1 = list()
list2 = list("ABCD")
list3 = list((1, 2, 3))
 
print (list1)
print (list2)
print (list3)

# Using Split()
mystr = "Selamat Pagi Semua"
myList = mystr.split()

print (myList, "\n") # output akan dipecah menjadi String Sendiri

# Data Access List 
myList = [1, 2, 3, 4, 5]
# 0 dimulai Dari 1
# -1 dimulai Dari 5
print(myList[0]) # output 1
print(myList[2]) # output 1
print(myList[-2]) # output 1
print(myList[-1], "\n") # output 1

# Data Change List
my_lst = [1, 2, [1, 2, 3]]
my_lst[0] = 100
print(my_lst) #Output: [100, 2, [1, 2, 3]]
my_lst[2][1] = 0
print(my_lst, "\n") #Output: [100, 2, [1, 0, 3]]

# Data Entering List
# method .append() digunakan untuk item yang dimasukkan ke parameter akan ditambahkan ke belakang list.
my_lst = []
my_lst.append(1)
print(my_lst) # Output: [1]
my_lst.append(2) 
print(my_lst) # Output: [1, 2]
my_lst.append("Hello")
print(my_lst, "\n") # Output: [1, 2, "Hello"]

# Method .insert() mengambil 2 parameter (i, elem) sedemikian sehingga elemen elem akan dimasukkan ke dalam list di index ke i.
my_lst = ["a", "b", "c", "d", "e"]
my_lst.insert(1, "o")
print(my_lst) # Output: ["a", "o", "b", "c", "d", "e"]
my_lst.insert(5, "p")
print(my_lst) # Output: ["a", "o", "b", "c", "d", "p", "e"]

# Remove Data List
# method .pop() digunakan untuk menghapus 1 parameter atau tanpa parameter.
my_lst = [1, 2, 3, 4, 5]

my_lst.pop(0)
print(my_lst) # Output: [1, 2, 3, 4]
my_lst.pop(2)
print(my_lst, "\n") # Output: [1, 2, 4]

# Remove2 Data List
# method .remove() untuk menghapus elemen di dalam list (Parameter).
my_lst = ["a", "b", "c", "b", "z"]
my_lst.remove("a")
print(my_lst) # Output: ["b", "c", "b", "z"]
my_lst.remove("b")
print(my_lst) # Output: ["c", "b", "z"]