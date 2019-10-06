# https://atcoder.jp/contests/abc125/tasks/abc125_a
# A - Biscuit Generator

a, b, t = list(map(int, input().split()))
i = 1
c = 0

while i <= (t + 0.5):
    if i % a == 0:
        c += b
    i += 1

print(c)