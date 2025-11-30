secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class find:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time 

find1 = find(secret_code, meeting_point, time)
print("secret code :", find1.secret_code)
print("meeting point :", find1.meeting_point)
print("time :", find1.time)