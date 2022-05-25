#WAP that randomly select a number between 1 to 5 and ask user to guess the number 3 times.
# if user guess the number correctly, print "you win"
# if user guess the number incorrectly, print "you lose"

import random

x = random.randint(1,5)

y = int(input("enter a number between 1 to 5: "))
print(x)
if y == x:
    print("you win")
else:
    print("you lose")
