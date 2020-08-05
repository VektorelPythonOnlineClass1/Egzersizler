# -*- coding: utf-8 -*-

#empty list
my_list = []
print(my_list)
print(type(my_list))

#list of integers
my_list = [1, 2, 3]
print(my_list)
print(type(my_list))

#list with mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)
print(type(my_list))

#nested list
my_list = ["mouse", [2, 3, 4], ['a']]
print(my_list)
print(type(my_list))

students = ["Hünkar","Semra","Gazanfer","Ümit"]
print(students[0])
print(students)
students.append("Genç")
print(students)
students.remove("Genç")
print(students)
students[0] = "Hünk"
print(students)

#List Constructor
cities = list(("Ankara","İstanbul"))
print(cities)
print(len(cities))

#Clear
# print(cities.clear())
# print(cities)
# print(len(cities))

#Count
print("Ankara sayısı = " + str(cities.count("Ankara")))

#Index
print("Ankara yeri = " + str(cities.index("Ankara")))

#Pop
cities.pop(1)
print(cities)

#Insert
cities.insert(0,"İstanbul")
print(cities)

#Reverse
cities.reverse()
print(cities)

#Verinin yedeğini almak
#cities2= cities
#cities2[0]="İzmir"
#print(cities)
#print(cities2)
#(Diziler referans tiptir. Bellekteki yere işaret eder. Yani ikisi de aynı yer aslında.)

cities3 = cities.copy()
cities2= cities
cities2[0]="İzmir"
print(cities)
print(cities2)
print(cities3)

#EXTEND
cities.extend(cities3)
cities.sort()
cities.reverse() #Tersten sıralamak istersek
print(cities)




















