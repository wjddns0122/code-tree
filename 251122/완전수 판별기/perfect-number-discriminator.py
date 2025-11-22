n = int(input())

# n의 약수(1 ~ n-1) 구하기
divisors = [i for i in range(1, n) if n % i == 0]

# 약수의 합
sum_val = sum(divisors)

# 완전수(Perfect number)인지 확인
if sum_val == n:
    print("P")
else:
    print("N")
