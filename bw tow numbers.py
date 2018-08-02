nm=int(input())
n,k=input().split()
n,k=int(n),int(k)
if (nm>n and nm<k) or (nm>k and nm<n):
    print("yes")
else:print("no")
