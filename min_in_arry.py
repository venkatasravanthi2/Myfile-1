nm=int(input())
storage= input()
storage = [int(x) for x in storage.split()]
print(min(storage[0:nm]))
