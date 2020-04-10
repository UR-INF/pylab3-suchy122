#zadanie 5
def happ(z, y):
    for i in range(len(y)):
        if z==y[i]:
            return 1
            break
        else:
            return 0
def finder(x):
    y=[]
    y.append(x[0])
    cntr = 0
    for z in range(len(x)):
        if x[0]==x[z]:
            cntr+=1
    print(x[0]+': '+str(cntr))
    for j in range(len(x)):
        cntr=0
        for i in range(len(x)):
            if x[j]==x[i]:
                cntr+=1
        f=x[j]
        if happ(f,y)==0:
            print(x[j]+': '+str(cntr))

x=input("Tekst:").replace(" ","")
finder(x)