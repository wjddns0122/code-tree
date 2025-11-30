user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self, user2_id = "codetree", user2_level = 10):
        self.user2_id = user2_id
        self.user2_level = user2_level

User1 = User()
print(f"user {User1.user2_id} lv {User1.user2_level}")
User2 = User(user2_id, user2_level)
print(f"user {User2.user2_id} lv {User2.user2_level}")