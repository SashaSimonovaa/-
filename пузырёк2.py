a = [8, 6, 7, 3, 1, 4]
for i in range(len(a)):
    for j in range(len(a)-1, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
print(*a)