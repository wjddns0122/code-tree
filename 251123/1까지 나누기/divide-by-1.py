n = int(input())
cnt = 0
result = 0 
for i in range(1, n + 1):
    if n % i == 0:
        result = int(n / i)
        cnt += 1
        if result == 0:
            break

cnt -= 1
print(cnt)