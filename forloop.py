# to write a python program that takes in command line argument as an input and print the number of arguments, list of arguments and first argument
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
sum = x + y
diff = x-y
mul= x*y
divi = x/y
modu = x % y
print("the sum is :",sum)
print("The subtraction is :", diff)
print("The multiplication is: ", mul)
print("the division is: ", divi)
print("The modlus is: ", modu)


