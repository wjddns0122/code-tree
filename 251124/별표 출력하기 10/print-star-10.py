# 변수 선언 및 입력
n = int(input())

# i가 짝수인 경우 별을 1개, 홀수인 경우 i + 1개 출력합니다
for i in range(2 * n):
	if i % 2 == 0:
		for _ in range(1 + i // 2):
			print("*", end=" ")
	else:
		for _ in range(n - (i - 1) // 2):
			print("*", end=" ")
	print()

### 와 이런 방법이... 그냥 1 3 2 2 3 1 이렇게 대칭점으로 푸는게 아니라
## 그냥 i += 1 일수록 2로 나누면 출력됌 
