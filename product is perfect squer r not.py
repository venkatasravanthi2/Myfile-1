nm,k=input().split()
nm,k=int(nm),int(k)
pro=nm*k
count=0
for i in range(0,pro):
    if i*i==pro:
        count=1
if count==1:
    print("yes")
else:print("no")
