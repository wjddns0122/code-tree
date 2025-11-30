class Person:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

n = int(input())
people = []

for _ in range(n):
    data = input().split()
    name = data[0]
    addr = data[1]
    city = data[2]
    people.append(Person(name, addr, city))

# Find the person with the lexicographically largest name (slowest)
slowest_person = people[0]
for person in people:
    if person.name > slowest_person.name:
        slowest_person = person

print(f"name {slowest_person.name}")
print(f"addr {slowest_person.addr}")
print(f"city {slowest_person.city}")