import math
nm,m=input().split()
nm=int(nm)
m=int(m)
k=''
if m < 10000:
    for i in range(nm+1,m):
        if i % 2 == 0 and i != 0:
            if(i < m-2):
                k=' '
            else:
                k=''
            print(i,end=k)



