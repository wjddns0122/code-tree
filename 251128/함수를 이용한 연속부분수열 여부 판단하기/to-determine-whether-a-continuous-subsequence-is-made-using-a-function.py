n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
i = 0
found = False  # 겹치는 구간(연속부분수열)을 찾았는지 표시

# 시작 위치 i를 0부터 n1 - n2 까지만 보면 됨
while i <= n1 - n2:
    j = 0

    # arr1의 i부터 arr2와 하나씩 비교
    while j < n2 and a[i + j] == b[j]:
        j += 1

    # j가 n2까지 갔다 = arr2 전체가 다 맞았다
    if j == n2:
        found = True
        break

    i += 1  # 시작 위치 한 칸 뒤로 이동

if found:
    print("Yes")
else:
    print("No")
