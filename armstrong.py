nm=int(input())
temp=nm
sum=0
order=len(str(nm))
while nm >0:
    dg=nm % 10
    sum+=dg**order
    nm=nm//10
if(temp==sum):
    print("yes")
else:
    print("no")
