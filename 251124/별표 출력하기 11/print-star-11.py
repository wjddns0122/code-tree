# n = int(input())
# num1 = 2 * n + 1
# num2 = 1 + n

# for i in range(2 * n + 1):
#     if i % 2 == 0:
#         print("* " * num1, end="")
#         print()
#     else:
#         print("*   " * num2, end="")
#         print()

# 변수 선언 및 입력
n = int(input())
	
# 2*n+1칸의 정사각형에서 i, j에 짝수가 들어가면 *을 출력합니다.
for i in range(2 * n + 1):
	for j in range(2 * n + 1):
		if i % 2 == 0 or j % 2 == 0:
			print("*", end=" ")
		else:
			print(" ", end=" ")
	print()
