nm=int(input())
count=0
sum=0
while nm>0:
    rem=nm%10
    sum=sum+rem
    nm=nm//10
print(sum)
