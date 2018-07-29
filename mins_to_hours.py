nm=int(input())
if nm >=60:
    count=nm%60
    hr=nm/60
    hr=int(hr)
    print(hr,count)
else:
    print('0',nm)
