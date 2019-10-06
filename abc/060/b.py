# https://atcoder.jp/contests/abc060/tasks/abc060_b
# B - Choose Integers
a, b, c = list(map(int, input().split()))
answer = 'NO'

def hantei(a, b, c):
    if a == 1:
        return 'YES'

    if b % 2 == 0 and c % 2 == 0:
        return 'YES'

    if b % 2 == 0 and c % 2 == 1:
        # 総和が奇数
        if a % 2 == 0:
            return 'NO'
    return 'YES'

print(hantei(a, b, c))

