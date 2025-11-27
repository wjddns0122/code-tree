arr = list(map(int, input().split()))  
result = []

# 반복문에서 마지막 숫자를 제외한 값 처리
for num in arr[:-1]:
    if num >= 260:
        break
    result.append(num)


# 총합과 평균 계산
total = sum(result)  # 모든 값 더하기
average = total / len(result) if len(result) > 0 else 0  # 평균 구하기 (0으로 나누는 오류 방지)

print(f"{total} {average:.1f}")
