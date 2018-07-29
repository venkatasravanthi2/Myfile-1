nm=int(input())
if(nm<=1000):
    storage= input()
    storage = [int(x) for x in storage.split()]

for i in range(0,nm):
    print(storage[i],i)
