nm=int(input())
num=nm
rev=0
while(nm > 0):
    t=nm%10
    rev=(rev*10)+t
    nm=nm//10
print(rev)
