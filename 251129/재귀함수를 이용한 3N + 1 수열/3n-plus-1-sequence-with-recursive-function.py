n = int(input())
cnt = 0
# Please write your code here.
while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = (3 * n) + 1
    cnt += 1

print(cnt)