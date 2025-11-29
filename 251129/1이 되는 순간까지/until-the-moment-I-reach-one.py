n = int(input())

def counting_one(n):
    # 기저조건: n이 1이면 더 이상 나눌 필요 없음 → 0번
    if n == 1:
        return 0
    
    # 짝수이면 2로 나누고, 한 번 연산했으니 +1
    if n % 2 == 0:
        return counting_one(n // 2) + 1
    # 홀수이면 3으로 나누고, 역시 +1
    else:
        return counting_one(n // 3) + 1

print(counting_one(n))
