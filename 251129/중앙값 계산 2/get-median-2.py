# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))

# 홀수 번째 수를 지날때마다 정렬을 진행한 후 가운데 값을 출력합니다.
for i in range(n):
    if i % 2 == 0:
        # 오름차순 정렬을 진행합니다.
        sorted_arr = sorted(arr[:i + 1])
        # 가운데 값을 출력합니다.
        print(sorted_arr[i // 2], end=" ")
