import os 
liste1 = list()
liste = os.listdir(os.getcwd())
for i in liste :
    if len(i) >5 :
        continue
    else:
        liste1.append(i)
print(liste1)