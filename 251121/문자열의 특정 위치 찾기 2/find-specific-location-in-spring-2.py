# 문자열 리스트를 정의합니다.
string = ["apple", "banana", "grape", "blueberry", "orange"]

# 영문자를 입력받습니다.
a = input()
cnt = 0

# 조건을 만족하는 문자열을 출력하고 조건을 만족하는 문자열의 개수를 셉니다.
for i in range(5):
	if string[i][2] == a or string[i][3] == a:
		print(string[i])
		cnt += 1

# 조건을 만족하는 문자열의 개수를 출력합니다.
print(cnt)
