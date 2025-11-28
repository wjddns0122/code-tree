s = input().strip()

# 문자열이 전부 같은 문자면 set의 길이가 1이 됨
if len(set(s)) == 1:
    print("No")
else:
    print("Yes")
