arr = list(map(int, input().split()))
a = []
b = []
for i in arr:
    if i % 2 == 0:
        b.append(i)
        
result1 = sum(b)

for num in arr:
    if num % 3 == 0:
        a.append(num)

result2 = sum(a) / len(a)

print(f"{result1} {result2:.1f}")