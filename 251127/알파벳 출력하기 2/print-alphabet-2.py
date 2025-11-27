n = int(input())
cnt = 'A'

for i in range(n):
    for j in range(n):
        if i > j:
            print(" ", end=" ")
        else:
            print(cnt, end=" ")
            cnt = chr(ord(cnt) + 1)
            if ord(cnt) > ord('Z'):
                cnt = 'A'

    print()