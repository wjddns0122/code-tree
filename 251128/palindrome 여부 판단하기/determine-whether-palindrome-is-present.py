# 변수 선언 및 입력:
string = input()


def palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True


if palindrome(string):
    print("Yes")
else:
    print("No")
