# WAP to find a max no. in a list
from operator import indexOf


list1 = [0, 7, 2, 5, 8, 3, 1, 4, 6]
x = max(list1)
print("maximum no. is ", x)
y = indexOf(list1, x)
print("index of max element is: ", y)