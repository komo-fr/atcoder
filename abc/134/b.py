# https://atcoder.jp/contests/abc134/tasks/abc134_b
# B - Golden Apple
import math

n, d = list(map(int, input().split()))

ans = math.ceil(n / float(2*d + 1))
print(ans)
