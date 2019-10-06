# https://atcoder.jp/contests/abc053/tasks/arc068_a
# C - X: Yet Another Die Game
import math
n = int(input().split()[0])

c = math.floor(n / 11) * 2

if n % 11 == 0:
    pass
elif n % 11 <= 6:
    c += 1
elif n % 11 > 6:
    c += 2

print(int(c))
