#!/usr/bin/env python3
import itertools
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

N, M = list(map(int, input().split()))
adj = np.zeros((N, N))
edge_list = []
for _ in range(M):
    u, v, l = list(map(int, input().split()))

    a = min(u, v)
    b = max(u, v)
    edge_list.append((a, b, l))

    if u != 1:
        adj[u-1, v-1] = l
        adj[v-1, u-1] = l

# ノード1に接続するエッジ以外について、全対の最短経路を求める
csr = csr_matrix(adj)
st_path = floyd_warshall(csr)

# 1と接続しているエッジ
e_list = [edge for edge in edge_list if (edge[0] == 1) or (edge[1] == 1)]
p_gen = itertools.combinations(e_list, 2)

min_cost = float('inf')
for p in p_gen:
    e_1, e_2 = p
    n_1, n_2 = e_1[1], e_2[1]
    shortest = st_path[n_1 - 1][n_2 - 1]
    cost = shortest + e_1[2] + e_2[2]
    if cost != float('inf'):
        min_cost = min(min_cost, cost)

ans = -1 if min_cost == float('inf') else int(min_cost)

print(ans)
