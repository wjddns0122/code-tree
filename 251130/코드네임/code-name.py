MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class myPerson:
    def __init__(self, codenames, scores):
        self.codenames = min(codenames)
        self.scores = min(scores)

myPerson1 = myPerson(codenames, scores)
print(myPerson1.codenames, myPerson1.scores)