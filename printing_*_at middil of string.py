nm=list(input())
f=len(nm)
kk=len(nm)/2
k=int(len(nm)/2)
if f%2==0:
    nm[k-1]="*"
    nm[k]="*"
else:nm[k]="*"
for i in range(0,len(nm)):
    print(nm[i],end='')
