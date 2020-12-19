#!/usr/bin/env python3
from collections import Counter
import itertools

H, W = list(map(int, input().split()))
a_table = []

for _ in range(H):
    a_list = list(map(int, input().split()))
    a_table.append(a_list)

N = H * W

all_a_list = itertools.chain.from_iterable(a_table)
counter = Counter(all_a_list)
goal = min(counter.keys())
c = 0
for k, v in counter.items():  # 10000
    if k == goal:
        continue
    c += (k - goal) * v
ans = c
print(ans)
