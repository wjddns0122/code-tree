n1, n2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

found = False  # arr2가 arr1 안에서 발견됐는지 표시하는 변수

# i는 arr1에서 시작 위치 (0번 인덱스부터 n1 - n2번 인덱스까지 볼 수 있음)
for i in range(n1 - n2 + 1):
    ok = True  # 이번 위치(i)에서 arr2가 딱 맞는지 확인하는 플래그

    # arr2의 모든 원소를 비교
    for j in range(n2):
        if arr1[i + j] != arr2[j]:
            ok = False   # 하나라도 다르면 실패
            break        # 더 볼 필요 없음

    if ok:          # 이번 i에서 전부 같았다 = arr2를 찾았다!
        found = True
        break        # 이미 찾았으니 더 돌 필요 없음

if found:
    print("Yes")
else:
    print("No")
