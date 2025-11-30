N = int(input())

class Student:

    def __init__ (self, height, weight, number):
        self.height, self.weight, self.number = height, weight, number

students = []

for _ in range(N):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight,_))


students.sort(key = lambda x : (-x.height, -x.weight, x.number))

for student in students:

    print(student.height, student.weight, student.number + 1)
