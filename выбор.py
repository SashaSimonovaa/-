a = [8, 6, 7, 3, 1, 4]
for i in range(len(a)):
    x = a[i]
    k = i
    for j in range(i+1, len(a)):
        if a[j] < x:
            k = j
            x = a[j]
    a[k] = a[i]
    a[i] = x
print(*a)