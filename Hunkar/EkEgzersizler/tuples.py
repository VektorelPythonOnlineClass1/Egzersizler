# -*- coding: utf-8 -*-
# listelere benzerdir.
# tek farkı listelerde elemanları değiştirebiliyorken, tuple da değiştirmek söz konusu değildir.
# bu veri yapısı performanslı bir data sağlar.

#empty tuple
my_tuple= ()
# print(my_tuple)

#tuple having integers
my_tuple = (1,2,3)
# print(my_tuple)

#tuple with mixed datatypes
my_tuple=(1,"Hello!",3.4)
# print(my_tuple)

#nested tuple
my_tuple=("string",[1,2,3],(4,5,6))
# print(my_tuple)

# Examples
tupleList = (2,4,6,"Ankara",(1,2,3),[1])
list=[2,4,6,"Ankara",[1,2,3],(1,2)]

# tupleList[0]=6 
#TypeError: 'tuple' object does not support item assignment
#list[0]=6

print(tupleList[-2]) #sağdan 2.
print(list[-2])

print(tupleList[2])
print(list[2])

print(tupleList[1:2])
print(list[1:2])

# print(type(tupleList))
# print(type(list))
# print(tupleList)
# print(list)
# print(len(tupleList))
# print(len(list))

# Eğer tek elemanlı bir tuple tanımlanıyorsa
tupleList2=("Hünkar",)
print(type(tupleList2))