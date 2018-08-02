nm=input()
count=0
count1=0
for i in range(0,len(nm)):
    if (nm[i]=='a' or nm[i]=='e' or nm[i]=='i' or nm=='o' or nm=='u'):
        count=1
if count==1:
    print("yes")
else:print("no")
