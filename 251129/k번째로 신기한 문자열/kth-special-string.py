n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

str.append(t)
str.append(t+"z")
str.sort()

print(str[str. index(t)+k])

