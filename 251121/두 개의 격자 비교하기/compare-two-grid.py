# 입력 받기
N, M = map(int, input().split())  # 격자의 행과 열 개수 입력 받기

# 첫 번째 격자 입력 받기
mat1 = [list(map(int, input().split())) for _ in range(N)]

# 두 번째 격자 입력 받기
mat2 = [list(map(int, input().split())) for _ in range(N)]

# 격자 비교하고 출력하기
for i in range(N):
    for j in range(M):
        if mat1[i][j] == mat2[i][j]:
            print(0, end=" ")  # 값이 같으면 0 출력
        else:
            print(1, end=" ")  # 값이 다르면 1 출력
    print()  # 한 줄 끝날 때마다 줄 바꿈
