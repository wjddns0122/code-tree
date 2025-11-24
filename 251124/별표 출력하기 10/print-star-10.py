n = int(input())

rows = 2 * n  # 전체 줄 수

for i in range(1, rows + 1):
    # 대칭 위치를 이용해서 윗부분 인덱스 j 계산
    if i <= n:
        j = i
    else:
        j = 2 * n + 1 - i   # 위쪽에서 대응되는 줄 번호

    # 윗부분 규칙에 따라 별 개수 정하기
    if j == 1:
        cnt = 1
    elif j == 2:
        cnt = n
    else:
        cnt = j - 1

    # 별 찍기 (* 사이에 공백 넣기)
    for k in range(cnt):
        print("*", end="")
        if k != cnt - 1:    # 마지막 별 뒤에는 공백 안 넣기
            print(" ", end="")
    print()
