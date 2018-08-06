a1 = [10, 45, 2, 56, 12, 34, 90, 27]
a2 = [45, 1, 89, 77, 2, 90, 100]
a1.sort()
for x in a1:
    if x in a2:
        print(x)
