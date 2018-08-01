nm=int(input())
i=0
while i<1000:

    if nm<2**i:
        print(2**i)
        break
    i+=1
