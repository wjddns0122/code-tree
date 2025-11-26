n = int(input())

for i in range(1, n + 1):   # i = 1, 2, 3, 4
    for j in range(1, i + 1):      # j = 1, 2, 3, 4
        print(i * j, end=" ")
    print() 