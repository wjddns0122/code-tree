a, b = list(map(int, input().split()))

while a <= b:
    print(a, end=" ")

    if a % 2 == 1:  # 홀수일 때
        if a * 2 <= b:
            a *= 2
        else:
            break
    elif a % 2 == 0:  # 짝수일 때
        if a + 3 <= b:
            a += 3
        else:
            break   