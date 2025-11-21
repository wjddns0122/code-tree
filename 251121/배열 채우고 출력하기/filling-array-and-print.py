n = input().split()
result = []

for i in range(len(n) - 1, -1, -1):
    result.append(n[i])

for i in range(len(result)):
    print(result[i], end="")