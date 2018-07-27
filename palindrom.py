nm=int(input())
num=nm
rev=0
while (num>0):
    count= num % 10
    rev =rev*10+count
    num=num//10
if(rev == nm):
    print("yes")
else:
    print("no")
