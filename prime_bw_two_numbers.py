nm,lm=input().split()
nm=int(nm)
lm=int(lm)

for i in range(nm+1,lm):
    count=0
    for j in range(1,i):
        if(i % j) == 0:
            count+=1
            if(count == 2):
                break
    else:
        if(j < nm+4):
            k=' '
        else:
            k=''
        print(j+1,end=k)
