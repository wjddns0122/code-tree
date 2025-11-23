n = int(input())
cnt = 0

while n <= 1000:
    if n % 2 == 0:
        cnt += 1
        n = (n * 3) + 1
    else:
        cnt += 1
        n = (n * 2) + 2

print(cnt)