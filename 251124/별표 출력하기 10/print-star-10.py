n = int(input())

rows = 2 * n  # 전체 줄 수

for i in range(1, rows + 1):
    # 위쪽/아래쪽 대칭을 위해 기준 줄 번호 t 만들기 (1 ~ n)
    if i <= n:
        t = i
    else:
        t = 2 * n + 1 - i  # 위쪽에서 대칭되는 줄 번호

    # t번째 줄에서 찍을 별 개수(cnt) 결정
    if t == 1:
        cnt = 1
    elif t == 2:
        cnt = n
    elif t == 3:
        cnt = 2
    else:  # t >= 4
        cnt = n - t + 3   # N-1, N-2, ..., 3 이런 식으로 내려감

    # 별 cnt개를 " *" 사이에 공백 넣어서 출력
    for k in range(cnt):
        print("*", end="")
        if k != cnt - 1:   # 마지막 별 뒤에는 공백 X
            print(" ", end="")
    print()
