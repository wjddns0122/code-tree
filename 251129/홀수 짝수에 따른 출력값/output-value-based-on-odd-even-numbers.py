n = int(input())


# 1부터 n까지의 n과 홀짝이 같은 수들의 합을 반환합니다.
def get_num(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # n과 홀짝이 같은 수만을 재귀함수로 호출합니다.
    return get_num(n - 2) + n


print(get_num(n))
