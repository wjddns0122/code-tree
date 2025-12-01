import sys

def solve():
    # 명령어를 문자열로 입력받습니다.
    commands = sys.stdin.readline().strip()
    
    # 초기 위치 (0, 0)
    x, y = 0, 0
    
    # 초기 방향: 북쪽 (North)
    # 0: 북, 1: 동, 2: 남, 3: 서
    dir_idx = 0
    
    # 북, 동, 남, 서 순서에 따른 dx, dy
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for cmd in commands:
        if cmd == 'L':
            # 왼쪽으로 90도 회전 (북 -> 서 -> 남 -> 동)
            dir_idx = (dir_idx - 1) % 4
        elif cmd == 'R':
            # 오른쪽으로 90도 회전 (북 -> 동 -> 남 -> 서)
            dir_idx = (dir_idx + 1) % 4
        elif cmd == 'F':
            # 현재 방향으로 한 칸 이동
            x += dx[dir_idx]
            y += dy[dir_idx]
            
    print(x, y)

if __name__ == "__main__":
    solve()