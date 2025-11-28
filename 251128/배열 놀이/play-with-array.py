n, q = map(int, input().split())     # n: 배열 원소 개수, q: 질의 개수
arr = list(map(int, input().split()))  # n개의 원소 입력

for _ in range(q):  # q번 질의 처리
    cmd = list(map(int, input().split()))  # 한 줄 질의 입력
    t = cmd[0]  # 질의 타입 (1, 2, 3 중 하나)

    # 1 x : x번째(1-based) 원소 출력
    if t == 1:
        x = cmd[1]
        print(arr[x - 1])

    # 2 v : 값 v가 배열에 있으면 그 위치(1-based) 출력, 없으면 0 출력
    elif t == 2:
        v = cmd[1]
        if v in arr:
            print(arr.index(v) + 1)  # index()는 0부터니까 +1
        else:
            print(0)

    # 3 l r : 구간 [l, r] (1-based)의 원소들 전부 출력
    elif t == 3:
        l, r = cmd[1], cmd[2]
        # 1-based이니까 파이썬 인덱스로 바꾸면 [l-1, r-1] → 슬라이스는 r은 포함 안되니 r 그대로
        print(*arr[l-1:r])
