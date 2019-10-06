# https://atcoder.jp/contests/abc065/tasks/arc076_a
# C - Reconciled?
import math

# (n+m) C (m)
# 犬同士と猿同士が隣り合わないようにする

N, M = list(map(int, input().split()))
mod = 10 ** 9 + 7

# 個体は識別されてる
if abs(N-M) <= 1:
    dog_p = math.factorial(N)
    monky_p = math.factorial(M)
    work = ((dog_p % mod) * (monky_p % mod)) % mod

    if N != M:
        ans = work
    else:
        ans = ((work % mod) * (2 % mod)) % mod
else:
    # 全匹並べられない
    ans = 0

print(ans)
