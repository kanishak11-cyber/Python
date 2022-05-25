# WAP to create an empty list and take input from user to add elements to the list and print the square root of odd numbers in the list
import math
lst = []
while True:
    n = int(input("Enter a number: "))
    # print("type -1 for exit the program")
    if n == -1:
        break
    lst.append(n)
print("The list is: ", lst)

for i in range(len(lst)):
    if lst[i] % 2 != 0:
        print("The square root of", lst[i], "is",(lst[i] ** 0.5) )


