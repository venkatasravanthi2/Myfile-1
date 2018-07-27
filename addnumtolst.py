nm,k=input().split()
nm=int(nm)
k=int(k)
a=[]
for i in range(0,nm):
    a.append(i+1)
    print(a[i],end=' ')
g=0
for j in range(0,k):
    g+=a[j]
print('\n',g)
