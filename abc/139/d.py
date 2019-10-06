# https://atcoder.jp/contests/abc139/tasks/abc139_d
# D - ModSum
import math

N = int(input().split()[0])

if (N - 1) % 2 == 0:
    ans = int(N * ((N - 1) / 2))
else:
    mean_v = ((N - 1) // 2) + 1
    ans = N * ((N - 1) // 2)
    ans += mean_v

print(ans)
