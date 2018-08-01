nm=input()
count=0
count1=0
for i in range(0,len(nm)):
    if (nm[i]>='a' and nm[i]<='z') or (nm[i]>'A' and nm[i]<'Z'):
        count=1
    elif (nm[i]=='1') or (nm[i]=='2') or (nm[i]=='3') or (nm[i]=='4') or (nm[i]=='5') or (nm[i]=='6') or (nm[i]=='7') or (nm[i]=='8') or (nm[i]=='9') or (nm[i]=='0'):
        count1=1
if count+count1==2:
    print("Yes")
else:print("No")
