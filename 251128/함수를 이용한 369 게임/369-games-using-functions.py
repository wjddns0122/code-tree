a, b = map(int, input().split())
cnt = 0
# Please write your code here.
for i in range(a, b + 1):
    if i % 3 == 0 or i // 10 == 3 or i // 10 == 6 or i // 10 == 9 or i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        cnt += 1

print(cnt)