# 변수 선언 및 입력:
a, b = tuple(map(int, input().split()))


# 해당 숫자가 소수인지 여부를 반환하는 함수를 작성합니다.
def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


# 자릿수의 합이 짝수인지 여부를 반환하는 함수를 작성합니다.
def is_digit_sum_even(n):
    digit_sum = (n // 100) + ((n // 10) % 10) + (n % 10)
    if digit_sum % 2 == 0:
        return True
    
    return False


# 해당 숫자가 소수이면서 자릿수의 합이 짝수인지 여부를 반환하는 함수를 작성합니다.
def judge_num(n):
    if is_prime(n) and is_digit_sum_even(n):
        return True
    
    return False


cnt = 0

for i in range(a, b + 1):
    if judge_num(i):
        cnt += 1


print(cnt)
