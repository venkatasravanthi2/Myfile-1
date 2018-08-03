num=int(input())
count=0
for i in range(1,num):
    if(num % i) == 0:
        count+=1
        if(count == 2):
            print("no")
            break
else:
    print("yes")
