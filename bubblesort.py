# WAP to implement bubble sort
lst = [5, 2, 4, 6, 1, 3]
for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)



