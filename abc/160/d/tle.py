#!/usr/bin/env python3
import collections
import numpy as np
from scipy.sparse.csgraph import shortest_path

N, X, Y = list(map(int, input().split()))

d_table = []
for i in range(N):  # 2 * 10 ** 3
    d_list = [0] * N
    if i != 0:
        d_list[i - 1] = 1
    if i != N - 1:
        d_list[i + 1] = 1
    d_table.append(d_list)

d_table[X - 1][Y - 1] = 1
d_table[Y - 1][X - 1] = 1
adj = np.array(d_table)
d_matrix = shortest_path(adj, method="FW")

counter = collections.Counter(list(d_matrix.flatten()))
ans_s = []
for k in range(1, N):  # 2 * 10 ** 3
    c = counter[float(k)]
    c = c // 2
    ans_s.append(str(c))
ans = "\n".join(ans_s)
print(ans)
