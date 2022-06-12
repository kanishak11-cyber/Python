# def factorial(n):
#     if(n==1):
#         return n
#     return n*(n-1)

# driver code
x = int(input("enter the number for factorial: "))
# if x == 0 or x == 1:
#     print("factorial of ",x,"is",1)
# else:
#     print("factorial of ",x,"is",factorial(x))
y = x 
if x < 0:
    print("factorial of ",y,"is not possible")
elif x == 0:
    print("factorial of ",y,"is",1)
else:
    factorial = 1
    while x > 0:
        factorial = factorial * x
        x = x - 1
    print("factorial of ",y,"is",factorial)