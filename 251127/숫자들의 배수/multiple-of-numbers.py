n = int(input())  # 입력받은 숫자
a = []
count_5 = 0  # 5의 배수가 나온 횟수

for num in range(n, n * 11, n):
    if num % 5 == 0:
        count_5 += 1  # 5의 배수가 나온 횟수 증가
        if count_5 == 2:  # 5의 배수가 두 번 나오면 종료
            a.append(num)
            break
    a.append(num)

# 출력
print(*a)