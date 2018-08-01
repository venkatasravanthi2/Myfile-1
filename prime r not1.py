nm=int(input())
count=0
for i in range(1,nm):
    if(nm % i) == 0:
        count+=1
        if(count == 2):
            print("no")
            break
else:
    print("yes")
