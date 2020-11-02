#!/usr/bin/env python3
import numpy as np

N, M, Q = list(map(int, input().split()))
adj_table = np.zeros((N, N))

x_list = []

adj_dict = {i + 1: [] for i in range(N)}

for _ in range(M):
    u, v = list(map(int, input().split()))
    # adj_table[u-1][v-1] = 1
    # adj_table[v-1][u-1] = 1
    adj_dict[u].append(v)
    adj_dict[v].append(u)

c_list = list(map(int, input().split()))
c_dict = {i + 1: c for i, c in enumerate(c_list)}

for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        print(c_dict[s[1]])
        for neighbor in adj_dict[s[1]]:
            c_dict[neighbor] = c_dict[s[1]]
    else:
        print(c_dict[s[1]])
        c_dict[s[1]] = s[2]
