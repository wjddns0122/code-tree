# 변수 선언 및 입력
n = int(input())
cnt = 'A'
	
# 알파벳을 정사각형 모양으로 출력합니다.
for _ in range(n):
	for _ in range(n):
		print(cnt, end="")
		cnt = chr(ord(cnt) + 1)
	print()
