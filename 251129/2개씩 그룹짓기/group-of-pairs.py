from collections import deque

num_of_groups = int(input())
numbers = list(map(int, input().split()))
groups: list[int] = [[0, 0]] # 인덱스 오류를 막기 위한 초기화

numbers = deque(sorted(numbers))

for _ in range(len(numbers) // 2): # 조어진 조건 상, 홀수일 일은 없음
    cur_small_value_index: int = 0
    while groups[-1] == [numbers[cur_small_value_index], numbers[-1]]:
        cur_small_value_index += 1
    groups.append([numbers.popleft(), numbers.pop()])

print(max(sum(group) for group in groups))
