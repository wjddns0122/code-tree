start, end = map(int, input().split())
cnt = 0

# 각 수에 대해 약수 합을 구하여 해당 수가 완전수인지 확인
for i in range(start, end + 1): 
    result = 0  # i의 약수 합을 저장할 변수
    for j in range(1, i):  # i의 약수를 구하는 부분
        if i % j == 0:  # 약수인 경우
            result += j  # 약수를 더함
    if result == i:  # 완전수일 경우
        cnt += 1  # cnt를 증가시킴

print(cnt)
