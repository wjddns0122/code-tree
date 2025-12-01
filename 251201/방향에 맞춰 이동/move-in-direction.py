# 변수 선언 및 입력
n = int(input())
x, y = 0, 0

# 동, 서, 남, 북 순으로 dx, dy를 정의합니다.
dx = [1, -1,  0, 0]
dy = [0,  0, -1, 1]

# 움직이는 것을 진행합니다.
for _ in range(n):
    c_dir, dist = tuple(input().split())
    dist = int(dist)
    
    # 각 방향에 맞는 번호를 붙여줍니다.
    if c_dir == 'E':
        move_dir = 0
    elif c_dir == 'W':
        move_dir = 1
    elif c_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3

    # 주어진 방향대로 dist 거리만큼 이동했을 경우의
    # 위치를 구해줍니다.
    x += dx[move_dir] * dist
    y += dy[move_dir] * dist
    
print(x, y)