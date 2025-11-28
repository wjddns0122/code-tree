a, b = map(int, input().split())

def is_prime(n):
    if n < 2:      # 0, 1은 소수가 아님
        return False
    for j in range(2, int(n**0.5) + 1):  # 2부터 √n까지
        if n % j == 0:
            return False
    return True

cnt = 0
for i in range(a, b + 1):
    if is_prime(i):
        cnt += i

print(cnt)
