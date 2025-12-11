n = 5
arrs = []

for _ in range(n):
    n, h, w = tuple(input().split())
    arrs.append((n, int(h), float(w)))

arrs.sort(key=lambda x: x[0])

print("name")
for n, h, w in arrs:
    print(n, h, w)
print()
arrs.sort(key=lambda x: -x[1])
print("height")
for n, h, w in arrs:
    print(n, h, w)