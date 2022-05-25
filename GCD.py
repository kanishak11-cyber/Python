#greatest comman divisor of two numbers

# import math
  
# print ("The gcd of 60 and 48 is : ",end="")
# print (math.gcd(60,48))

def GCD(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd
a = 60
b= 48
print ("The gcd of 60 and 48 is : ",end="")
print (GCD(60,48))