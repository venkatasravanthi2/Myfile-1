nm=input()
count=0
for i in range(0,len(nm)):
    if nm[i]=='0' or nm[i]=='1':
        count+=1
if count==len(nm):
    print("yes")
else:print("no")
