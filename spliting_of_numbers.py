nm=int(input())
a=[]
rev=0

count=0
while nm>0:
    temp=nm%10
    rev=rev*10+temp
    nm=nm//10
    count+=1
while rev>0:
    temp=rev%10
    a.append(temp)
    rev=rev//10
for i in range(0,count):
    if i<count-1:
        k=' '
    else:k=''
    print(a[i],end=k)
