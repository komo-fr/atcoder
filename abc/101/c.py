# https://atcoder.jp/contests/abc101/tasks/arc099_a
# C - Minimization
import math
N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

min_x = min(a_list)
min_x_i_list = [i for i, a in enumerate(a_list) if a == min_x]

c = 0

# 最初のi
start_x_i = min_x_i_list[0]
# 最初に左側を、できるだけ無駄がでないようにして埋める
if start_x_i + 1 < K:
    index = K - 1
    c += 1
else:
    x = math.ceil(start_x_i / (K - 1))
    index = (K - 1) * x
    c += x

while index < N - 1:  # 10 ** 5
    # index < j <= index + Kの範囲にmin_xがいるか
    next_min_list = [y for y in min_x_i_list if (index < y) and y <= (index + K)]
    if next_min_list:
        index += K
        c += 1
    else:
        index += K - 1
        c += 1

print(c)