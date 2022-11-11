a = [8, 6, 7, 3, 1, 4]
right = len(a)
left = 0
while right > left:
    for j in range(right-1, left, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
    right -= 1
    for j in range(left, right+1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
    left += 1
print(*a)