a = [8, 6, 7, 3, 1, 4]
for i in range(1, len(a)):
    k = a[i]
    j = i - 1
    while j >= 0 and k < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = k
print(*a)