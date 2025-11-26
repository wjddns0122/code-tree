n = int(input())

for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if i - j <= 0:
            print(j, end=" ")
    print()