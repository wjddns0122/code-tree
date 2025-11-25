n = int(input())      # 정사각형의 크기
cnt = 1    # 수의 시작 값
arr = [[0 for _ in range(n)] for _ in range(n)] # 1단계: 2차원 배열 만들기

# 2단계: 열 순서로 순회하기
for i in range(n):
    # i는 i번째 행이 아닌 i번째 열을 의미합니다.
    
    # 3단계: 짝수 열과 홀수 열 구분하여 값 채우기
    if i % 2 != 0:
        for j in range(n - 1, -1, -1):
            arr[j][i] = cnt
            cnt += 1
            if (cnt == n + 1):
                cnt = 1
    else:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1
            if (cnt == n + 1):
                cnt = 1

# 4단계: 출력하기
for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()

