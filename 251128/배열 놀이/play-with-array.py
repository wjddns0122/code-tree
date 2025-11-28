n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    t = query[0]   # 질의 타입

    # 1 x : x번째 원소 출력 (1-based)
    if t == 1:
        x = query[1]
        print(arr[x - 1])

    # 2 v : 값 v가 배열에 있으면 그 인덱스(1-based) 출력, 없으면 0 출력
    elif t == 2:
        v = query[1]
        if v in arr:
            print(arr.index(v) + 1)  # index()는 0-based니까 +1
        else:
            print(0)

    # 3 l r : l번째부터 r번째까지 원소들 출력 (1-based, 구간)
    elif t == 3:
        l, r = query[1], query[2]
        # l, r이 1-based니까 파이썬 슬라이싱에 맞게 l-1:r
        print(*arr[l-1:r])
