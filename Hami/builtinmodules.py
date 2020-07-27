# from 
# import 
# # 1.
# import os
# os.getcwd()
# os.path
# # 2.
# from os import path,getcwd
# getcwd()

# import random as rnd
# rnd.random()
# from random import random as rnd
# rnd()


# import os
# print(os.getcwd()) # get current working directory
# # "." current directory for python
# # ".." parent directory form python
# print(os.listdir())


"""import os
print(os.getcwd())
print(os.listdir())
"""
import random as rnd 
liste=["hami","hikmet","busra","hunkar","kagan","selim"]
print(rnd.choice(liste))
print(rnd.sample(liste,2))
rnd.shuffle(liste)
print(liste)