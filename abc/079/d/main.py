#!/usr/bin/env python3
import numpy as np
from scipy.sparse.csgraph import shortest_path

H, W = list(map(int, input().split()))

c_table = []

for _ in range(10):
    c_table.append(list(map(int, input().split())))

a_table = []

for _ in range(H):
    a_table.append(list(map(int, input().split())))

c_table = np.array(c_table)
a_table = np.array(a_table)

d_matrix = shortest_path(c_table)
cost = 0

for h in range(H):
    a_list = a_table[h]
    for a in a_list:
        if a == -1:
            continue
        cost += d_matrix[a][1]

ans = int(cost)
print(ans)
