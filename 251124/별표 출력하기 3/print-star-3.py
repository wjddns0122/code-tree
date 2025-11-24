n = int(input())

cnt = n * 2 -1
emp = 0
for _ in range(n):
    print(' ' * emp, end = '')
    print('* ' * cnt)
    cnt -= 2
    emp += 2