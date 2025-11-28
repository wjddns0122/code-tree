a, b = map(int, input().split())
cnt = 0

def is_369(n):
    # 1) 3의 배수이면 바로 True
    if n % 3 == 0:
        return True
    
    # 2) 각 자리 수에 3, 6, 9가 있는지 확인
    while n > 0:
        digit = n % 10       # 가장 오른쪽 자리
        if digit in (3, 6, 9):
            return True
        n //= 10             # 한 자리 줄이기
    
    return False             # 위에 안 걸리면 False

for i in range(a, b + 1):
    if is_369(i):
        cnt += 1

print(cnt)
