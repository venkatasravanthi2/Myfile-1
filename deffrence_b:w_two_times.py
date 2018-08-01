nm,k=input().split()
hm,kk=input().split()
nm,k,hm,kk=int(nm),int(k),int(hm),int(kk)
mn=0
if hm<nm:
    if kk>k:
        d=60-kk
        mn=d+k
        nm=nm-1
    hr=nm-hm
else:
    hr=hm-nm
    mn=kk-k
print(hr,mn)

