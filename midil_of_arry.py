nm=int(input())
if(nm<=1000):
    storage= input()
    storage = [int(x) for x in storage.split()]
    kk=sorted(storage[0:nm])
mn=(nm+1)/2
mn=int(mn)
print(kk[mn-1])
