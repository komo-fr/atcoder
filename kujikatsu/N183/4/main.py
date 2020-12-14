#!/usr/bin/env python3
from collections import Counter
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

N, X, Y = list(map(int, input().split()))

adj = np.zeros((N, N))

for i in range(N - 1):
    # print(f"({i}, {i+1})")
    adj[i][i + 1] = 1
    adj[i + 1][i] = 1

adj[X - 1][Y - 1] = 1
adj[Y - 1][X - 1] = 1

# print(adj)

csr = csr_matrix(adj)
d_matrix = shortest_path(csr, method="FW")

# print(f"{d_matrix=}")

counter = Counter(d_matrix.flatten().tolist())

for k in range(1, N):
    print(counter[k] // 2)
