n = int(input())
cnt = 0

for i in range(1, n + 1):
    cnt += i
    if cnt >= n:
        cnt = cnt - i
        break

print(cnt)