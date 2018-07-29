nm=int(input())
if(nm<=1000):
    storage= input()
    storage = [int(x) for x in storage.split()]
    kk=sorted(storage[0:nm])
for i in range(0,nm):
    if(i<nm-1):
        k=' '
    else:
        k=''
    print(kk[i],end=k)
