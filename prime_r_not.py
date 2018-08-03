num=int(input())
count=0
for x in range(1,num):
    if(num % x) == 0:
        count+=1
        if(count == 2):
            print("no")
            break
else:
    print("yes")
