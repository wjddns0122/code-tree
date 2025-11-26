n = int(input())

for i in range(n):
    print("  " * i, end="")
    # 숫자 출력
    for j in range(n - i, 0, -1):
        print(j, end=" ")
    print()  # 줄바꿈 
