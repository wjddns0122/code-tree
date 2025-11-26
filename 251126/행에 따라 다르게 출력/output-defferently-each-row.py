n = int(input())
cnt = 0

for i in range(n):
    for j in range(n):
        cnt += 1
        if i % 2 == 1:
            cnt += 1
            print(cnt, end=" ")
        else:
            print(cnt, end=" ")
    print()