a = [8, 6, 7, 3, 1, 4]
for i in range(len(a)):
    last = 0
    for j in range(len(a)-1, last, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            last = j
print(*a)