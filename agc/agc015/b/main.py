#!/usr/bin/env python3
import numpy as np
from scipy.sparse.csgraph import shortest_path

S = input()
N = len(S)
adj_table = []
count = 0
for i in range(1, N + 1):
    if S[i - 1] == "U":
        c = (i - 1) * 2 + (N - i)
    else:
        c = (i - 1) + (N - i) * 2
    count += c

ans = count
print(ans)
