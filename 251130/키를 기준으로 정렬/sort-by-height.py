# 변수 선언 및 입력
n = int(input())
students = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    students.append((name, int(height), int(weight)))

# Custom Comparator를 활용한 정렬
students.sort(key = lambda x: x[1])

# 출력
for name, height, weight in students:
    print(name, height, weight)
