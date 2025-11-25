n = int(input())
cnt = 1

for i in range(n):
    row = []

    for j in range(n):
        row.append(cnt)
        cnt += 1
        if (cnt == n + 1):
            cnt = 1

    if i % 2 != 0:
        for j in range(n - 1, -1, -1):
            print(row[j], end="")
    else:
        for j in range(n):
            print(row[j], end="")

    print()
