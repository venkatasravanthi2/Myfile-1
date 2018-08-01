nm,k=input().split()
nm,k=int(nm),int(k)
lst=[int(x) for x in input().split()]
count=0
for i in range(0,nm):
    if k==lst[i]:
        print("yes")
        break
else:print("no")
