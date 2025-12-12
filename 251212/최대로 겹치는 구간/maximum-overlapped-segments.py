# 입력 받기
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 1. 좌표 조정 (Offset)
# -100 ~ 100 범위를 커버해야 하므로 0 ~ 200으로 변환하기 위해 +100을 해줍니다.
OFFSET = 100
MAX_RANGE = 205  # -100~100은 크기가 200이므로 넉넉하게 잡습니다.

block = [0] * MAX_RANGE

for x1, x2 in segments:
    # 2. 음수 처리를 위해 OFFSET 더하기
    start = x1 + OFFSET
    end = x2 + OFFSET
    
    # 3. [중요] 끝점 제외하고 반복문 돌리기
    # "끝점에서 닿는 경우는 겹치지 않음" -> range(start, end)
    # 예: 1~3구간이면 1, 2번 인덱스에만 표시 (구간의 길이만큼 칠하기)
    for i in range(start, end):
        block[i] += 1

# 최댓값 출력
print(max(block))