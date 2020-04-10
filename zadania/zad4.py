#zadanie 4
import numpy as np
a=np.zeros((5,5),np.int64)
for i in range(len(a)):
    if i==0:
        a[i]=[2,3,4,5,6]
    else:
        a[i]=pow(a[i-1],2)
print(a)
