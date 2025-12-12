n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
block = [0] * 101

for a, b in segments:
    for i in range(a, b + 1):
        block[i] += 1

max_num = max(block)
print(max_num)