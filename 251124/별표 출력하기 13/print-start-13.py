n = int(input())
a1, a2 = n, 1
for i in range(2 * n):
    if i % 2 == 0:
        print('* '* a1,end='')
        a1 -= 1
    else:
        print('* '* a2,end='')
        a2 += 1
    print()
