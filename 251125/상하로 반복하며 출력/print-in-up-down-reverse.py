# 변수 선언 및 입력
n = int(input())
	
# 상하로 반복하여 출력합니다.
for i in range(n):
	for j in range(n):
		if j % 2 == 0:
			print(i + 1, end="")
		else:
			print(n - i, end="")
	print()
