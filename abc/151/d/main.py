#!/usr/bin/env python3
import numpy as np
from scipy.sparse.csgraph import shortest_path

H, W = list(map(int, input().split()))
s_table = []
node_index = 0

for _ in range(H):
    s_list = list(input())
    s_table.append(s_list)

adj = [[0] * (W * H) for _ in range(W * H)]
node_index = -1
for h_i, s_list in enumerate(s_table):
    for w_i, s in enumerate(s_list):
        node_index += 1
        if s == "#":
            continue
        if w_i + 1 < W:
            # 右隣と隣接しているか
            if s_list[w_i + 1] == ".":
                adj[node_index][node_index + 1] = 1
                adj[node_index + 1][node_index] = 1
        if h_i + 1 < H:
            # 下と隣接しているか
            if s_table[h_i + 1][w_i] == ".":
                adj[node_index][(h_i + 1) * W + w_i] = 1
                adj[(h_i + 1) * W + w_i][node_index] = 1

adj = np.array(adj)
d_matrix = shortest_path(adj)

d_matrix[d_matrix == float("inf")] = -1
ans = int(d_matrix.max())
print(ans)
