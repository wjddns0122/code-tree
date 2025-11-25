n = int(input())
cnt = 0

for i in range(n):
    for j in range(n):
        cnt += 2
        if cnt == 10:
            cnt = 0
            cnt += 2
        print(cnt, end=" ")
    print()