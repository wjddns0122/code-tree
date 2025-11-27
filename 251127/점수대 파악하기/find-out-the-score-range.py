# 배열에 주어진 수를 입력받아 저장합니다.
arr = list(map(int, input().split()))
count_arr = [0] * 11

# 카운팅 배열을 통해 십의 자리수 각각의 빈도 저장, 0이 나오면 for문에서 빠져나오기
for elem in arr:
	if elem == 0:
		break
	if elem < 10:
		continue
	count_arr[elem // 10] += 1
	
# 100점대부터 10점대까지 나온 횟수를 출력
for i in range(10, 0, -1):
	print(f"{i}0 - {count_arr[i]}")
