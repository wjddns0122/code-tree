text = input()
pattern = input()

# Please write your code here.

def find_pattern():
    for i in range(len(text)-len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1

print(find_pattern())