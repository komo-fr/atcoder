# https://atcoder.jp/contests/abc124/tasks/abc124_a
# A - Buttons

a, b = list(map(int, input().split()))

c = 0

for _ in range(2):
    if a >= b:
        c += a
        a -= 1
    else:
        c += b
        b -= 1

print(c)