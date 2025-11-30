n = int(input())
students = []

for _ in range(n):
    name, subject1, subject2, subject3 = tuple(input().split())
    students.append((name, int(subject1), int(subject2), int(subject3)))

students.sort(key = lambda x: x[1] + x[2] + x[3])

for name, subject1, subject2, subject3 in students:
    print(name, subject1, subject2, subject3)