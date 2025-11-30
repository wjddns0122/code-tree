n, b = map(int, input().split())  # 예: 111 4

def to_base(n, base):
    if n == 0:
        return "0"

    digits = []
    while n > 0:
        digits.append(str(n % base))  # 나머지가 해당 진수의 한 자리
        n //= base                    # 몫으로 갱신

    return ''.join(reversed(digits))  # 뒤집어서 문자열로

print(to_base(n, b))
