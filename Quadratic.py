import math
def quadratic(a,b,c):
  a = int(input("Please input a:"))
  b = int(input("Please input b:"))
  c = int(input("Please input c:"))
  delta = b*b - 4*a*c
  if delta < 0:
    print "There hasn't any solution,delta can not less than zero"
   x1 = -b + math.sqrt(delta)
   x2 = -b - math.sqrt(delta)
   if x1 == x2:
    print "x1=x2=",x1
   else:
    print "x1=",x1,"x2=",x2 
