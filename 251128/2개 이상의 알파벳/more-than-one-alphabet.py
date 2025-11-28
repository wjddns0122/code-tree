A = input()

def sd(s):
    # 인접한 두 글자만 비교하면 되니까 len(s) - 1 까지만
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False   # 나쁜 경우 발견 → False
    return True            # 끝까지 문제 없으면 True

if sd(A):
    print("Yes")
else:
    print("No")
