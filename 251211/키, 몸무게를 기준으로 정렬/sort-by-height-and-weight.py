n = int(input())
arr = []

for _ in range(n):
    n, h, w = tuple(input().split())
    arr.append((n, int(h), int(w)))

arr.sort(key=lambda x:(x[1], -x[2]))

for n, h, w in arr:
    print(n, h, w)