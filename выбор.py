N = int(input())
a = [i for i in map(int, input().split())]
for i in range(0, N):
    x = a[i]
    k = i
    for j in range(i+1, N):
        if a[j] < x:
            k = j
            x = a[j]
    a[k] = a[i]
    a[i] = x
print(a)