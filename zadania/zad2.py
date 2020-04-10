#zadanie 2
def rev():
    list=[]
    i=0
    print("Wpisz dane! Aby zakończyć wpisywanie wpisz q!")
    while True:
        x=input("Dane: ")
        if x!="q!":
            list.append(x)
            i+=1
        else:
            break
    z = len(list)
    for z in range(len(list)-1,-1,-1):
        print(list[z])
rev()