N, a = map(int, input().split())

i = 1  # 1부터 시작
while i <= N:
    if i % a == 0:
        print(1)
    else:
        print(0)
    i += 1   # i를 1씩 증가시키면서 1,2,3,...,N 검사
