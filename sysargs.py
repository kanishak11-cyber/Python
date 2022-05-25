import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = len(sys.argv)
print("The number of argument :", z)
for i in range(z):
    print(sys.argv[i])