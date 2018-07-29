nm=int(input())
storage= input()
storage = [int(x) for x in storage.split()]
print(max(storage[0:nm]))
