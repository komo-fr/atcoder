# https://atcoder.jp/contests/abc095/tasks/abc095_b
# B - Bitter Alchemy
import math

n, x = list(map(int, input().split()))
m_list = []

for _ in range(n):
    m_list.append(int(input().split()[0]))

nokori_x = x - sum(m_list)
min_m = min(m_list)
ans = math.floor(nokori_x / min_m + n)

print(ans)
