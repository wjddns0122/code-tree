n = input()
sentence = n.split()
if len(sentence[0]) > len(sentence[1]):
    print(sentence[0], len(sentence[0]))
elif len(sentence[0]) < len(sentence[1]):
    print(sentence[1], len(sentence[1]))
else:
    print("same")