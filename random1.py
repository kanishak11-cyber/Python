import random
n=3
x = random.randint(1,5)
while n > 0:

    y = int(input("enter a number between 1 to 5: "))
    print(x)
    if y == x:
        print("you win")
    else:
        print("you lose")
    n-=1