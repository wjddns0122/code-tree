arr = list(map(int, input().split()))  
result = []

for num in arr:
    if num >= 250:
        break
    result.append(num)

total = sum(result)  
average = total / len(result) if len(result) > 0 else 0  # 평균 구하기 (0으로 나누는 오류 방지)

print(f"{total} {average:.1f}")
