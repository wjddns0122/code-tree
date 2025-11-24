n = int(input())

for i in range(1, n + 1):       # i = 1, 2
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("@", end=" ")
    print()

for i in range(1, n):
    for j in range(n - i):  # i = 1
        print("@", end=" ")
    print()