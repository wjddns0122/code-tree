arr = input().split()

a, b = int(arr[0]), int(arr[1])

if a // b == 0:
    c = '0.'
else:
    c = str(a // b) + '.'
a = a % b
for _ in range(20):
    a = a * 10
    c += str(a // b)
    a = a % b
print(c)