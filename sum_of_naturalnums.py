m=int(input())
count=0
kk=0
if (m >=1):
    for i in range(1,m+1):
        for n in range(1,i):
            if(i % n)==0:
                count+=1
                if(count == 2):
                    break
        kk=kk+i
print(kk)
