
sm = int(input())

if (sm % 4) == 0:
   if (sm % 100) == 0:
       if (sm % 400) == 0:
           print("yes")
       else:
           print("no")
   else:
       print("yes")
else:
   print("no")
