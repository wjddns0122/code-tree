# 변수 선언 및 입력
dirs = input()
x, y = 0, 0
curr_dir = 3

# 동, 남, 서, 북 순으로 dx, dy를 정의합니다.
dxs = [1,  0, -1, 0]
dys = [0, -1,  0, 1]

# 움직이는 것을 진행합니다.
for c_dir in dirs:
    # 반시계방향 90' 회전
    if c_dir == 'L':
        curr_dir = (curr_dir - 1 + 4) % 4
    # 시계방향 90' 회전
    elif c_dir == 'R':
        curr_dir = (curr_dir + 1) % 4
    # 직진
    else:
        x, y = x + dxs[curr_dir], y + dys[curr_dir]

print(x, y)
