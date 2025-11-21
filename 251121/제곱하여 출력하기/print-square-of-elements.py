# 변수 선언 및 입력
n = int(input())

# 배열에 주어진 수를 입력받아 저장합니다.
arr = list(map(int, input().split()))

# n개의 정수를 제곱한 배열을 새로 만듭니다.
new_arr = [elem * elem for elem in arr]

# n개의 정수를 출력합니다.
for i in range(n):
	print(new_arr[i], end=" ")
