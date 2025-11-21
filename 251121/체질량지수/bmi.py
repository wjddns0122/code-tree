h, w = list(map(int, input().split()))

result = (10000 * w) / (h * h)
if result >= 25:
    print(result)
    print("Obesity")
else:
    print(result)