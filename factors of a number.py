nm=int(input())
for i in range(1,nm+1):
    if nm%i==0:
        if i<nm:
            k=' '
        else:k=''
        print(i,end=k)
