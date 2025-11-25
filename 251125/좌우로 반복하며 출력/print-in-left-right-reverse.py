# 변수 선언 및 입력
n = int(input())
	
# 좌우로 반복하여 출력합니다.
for i in range(n):
	for j in range(n):
		if i % 2 == 0:
			print(j + 1, end="")
		else:
			print(n - j, end="")
	print()
