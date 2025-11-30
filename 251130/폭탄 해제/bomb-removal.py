unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class bomb:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

bomb1 = bomb(unlock_code, wire_color, seconds)
print("code :", bomb1.unlock_code)
print("color :", bomb1.wire_color)
print("second :", bomb1.seconds)