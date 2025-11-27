n = int(input())
cnt = 64    # chr(65)

for i in range(1,n + 1):
    for j in range(i):
        cnt += 1
        if ord('Z') + 1 == cnt:
            cnt = 64
            cnt += 1
            print(chr(cnt), end="")
        else:
            print(chr(cnt), end="")
    print()