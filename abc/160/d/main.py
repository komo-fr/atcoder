#!/usr/bin/env python3
import collections
from collections import defaultdict

N, X, Y = list(map(int, input().split()))

skip_d = abs(X - Y)
d_count = defaultdict(lambda: 0)
# d_table = []
for i in range(N):
    # d_list = []
    for j in range(N):
        if i == j:
            d = 0
            d_count[d] += 1
            # d_list.append(d)
            continue
        # Normal
        min_index = min(i, j)
        max_index = max(i, j)

        if min_index <= X - 1 and Y - 1 <= max_index:
            # 両方外にいる
            d = abs(i - j) - skip_d + 1
        elif X - 1 <= min_index and max_index <= Y - 1:
            # 両方中にいる
            d_1 = abs(i - j)
            x2min = abs(min_index - (X - 1))
            max2y = abs((Y - 1) - max_index)
            d_2 = x2min + max2y + 1
            d = min(d_1, d_2)
        elif max_index <= Y - 1:
            # elif min_index <= X - 1 and X - 1 <= max_index < Y - 1:
            # 大きい方が中にいる
            d_1 = abs(i - j)
            max2y = abs((Y - 1) - max_index)
            min2y = abs(min_index - (Y - 1)) - skip_d + 1
            d_2 = max2y + min2y
            d = min(d_1, d_2)
        elif X - 1 <= min_index:
            # elif X - 1 <= min_index < Y - 1 and Y - 1 <= max_index:
            # 小さい方が中にいる
            d_1 = abs(i - j)
            d_2 = (abs(max_index - (X - 1)) - skip_d + 1) + abs((X - 1) - min_index)
            d = min(d_1, d_2)

        # d_list.append(d)
        d_count[d] += 1
    # d_table.append(d_list)

ans_s = []
for k in range(1, N):  # 2 * 10 ** 3
    c = d_count[k]
    c = c // 2
    ans_s.append(str(c))
ans = "\n".join(ans_s)
print(ans)
