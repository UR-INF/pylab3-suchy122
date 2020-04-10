#zadanie 3
import random
lista=[]
with open('zad3.txt','w') as f:
    for i in range(6):
        lista.append(round(random.uniform(-5,5),2))
        f.write(str(lista[i])+' ')