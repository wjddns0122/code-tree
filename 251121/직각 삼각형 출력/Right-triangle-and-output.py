n = int(input())

for i in range(1, n + 1):
    for _ in range(1,i * 2):
        print('*',end='')
    print()