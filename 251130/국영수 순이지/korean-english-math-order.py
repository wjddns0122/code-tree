# 변수 선언 및 입력
n = int(input())
students = []
for _ in range(n):
    name, kor, eng, math = tuple(input().split())
    students.append((name, int(kor), int(eng), int(math)))

# Custom Comparator를 활용한 정렬
students.sort(key = lambda x: (-x[1], -x[2], -x[3]))

# 출력
for name, kor, eng, math in students:
    print(name, kor, eng, math)
