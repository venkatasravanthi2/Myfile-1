nm,k=input().split()
nm,k=int(nm),int(k)
if nm>k:
    temp=nm-k
else:temp=k-nm
if temp%2==0:
    print("even")
else:print("odd")
