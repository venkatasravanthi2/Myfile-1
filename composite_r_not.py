nm=int(input())
count=0
for i in range(2,nm):
    if nm%i==0:
        count+=1
if count>1:
    print("yes")
else:print("no")
