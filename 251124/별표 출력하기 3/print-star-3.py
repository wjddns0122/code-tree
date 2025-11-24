# 변수 선언 및 입력
n = int(input())

# 모양에 맞게 별을 출력합니다.
for i in range(n):
	for _ in range(i):
		print(" ", end=" ")
	for _ in range((2 * n) - (2 * i) - 1):
		print("*", end=" ")
	print()