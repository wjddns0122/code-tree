# 변수 선언 및 입력
dir, foward = list(map(str, list(input())))
# 초기 상태가 북쪽을 향해야 하므로 
x, y = 0, 1

# 동, 서, 남, 북 순으로 dx, dy를 정의합니다.
dx = [1, -1,  0, 0]
dy = [0,  0, -1, 1]

if dir == "L":
    # 왼쪽으로 가면 서쪽으로 이동해야함
    if foward == "F":
        x, y = dx[1], dy[1]

elif dir == "R":
    if foward == "F":
        x, y = dx[0], dy[0]

print(x, y)