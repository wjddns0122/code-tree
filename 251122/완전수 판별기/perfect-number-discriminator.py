# 변수 선언, 입력
n = int(input())
sum_val = 0

# 1부터 n-1까지의 수 중에서 약수를 찾습니다.
for i in range(1, n):
    if n % i == 0:
        sum_val += i

# sum_val과 n이 같다면 P을, 다르다면 N을 출력합니다.
if sum_val == n:
	print("P")
else:
    print("N")
