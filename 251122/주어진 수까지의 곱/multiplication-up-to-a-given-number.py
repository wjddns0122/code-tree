a, b = list(map(int, input().split()))
mul = 1
for i in range(a, b + 1):
    mul *= i
    
print(mul)