#linear search

list1 = [1,0,4,2,7,3,6,5]
x = int(input("enter a number to search: "))
for i in range(0,len(list1)):
    if list1[i] == x:
        print("found at index: ",i)
        break
else:
    print("not found")
    