a=input()
if len(a)<100000:
    for i in range(1,len(a)+1):
        print (a[-i],end='')
