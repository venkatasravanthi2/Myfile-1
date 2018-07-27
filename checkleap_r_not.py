
asm = int(input())

if (asm % 4) == 0:
   if (asm % 100) == 0:
       if (asm % 400) == 0:
           print("yes")
       else:
           print("no")
   else:
       print("yes")
else:
   print("no")
