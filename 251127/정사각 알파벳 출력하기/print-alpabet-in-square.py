n = int(input())
x = 'A'
cnt = 0

for i in range(n):
    for j in range(n):
        print(chr(ord(x) + cnt), end="")
        cnt += 1
    print()