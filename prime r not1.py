nm=int(input())
coun=0
for i in range(1,nm):
    if(nm % i) == 0:
        coun+=1
        if(coun == 2):
            print("no")
            break
else:
    print("yes")
