# 변수 선언 및 입력
n = int(input())
sum_val = 0

# 1부터 증가시키며 더한 값이 n이상이 된 순간, 더해진 숫자를 출력합니다.
for i in range(1, 101):
	sum_val += i
	if sum_val >= n:
		print(i)
		break
