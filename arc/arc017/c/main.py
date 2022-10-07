#!/usr/bin/env python3
import itertools
from collections import defaultdict
N, X = list(map(int, input().split()))
w_list = []

for _ in range(N):
    w = int(input().split()[0])
    w_list.append(w)

a_n = N // 2
a_list = w_list[:a_n+1]
b_list = w_list[a_n+1:]

ap_gen = itertools.product([True, False],repeat=a_n)
bp_gen = itertools.product([True, False],repeat=N-a_n)

a_dict = defaultdict(lambda: 0)

for pattern in ap_gen:
    cost = 0
    for i, p in enumerate(pattern):
        cost += w_list[i]
    a_dict[cost] += 1

b_dict = defaultdict(lambda: 0)
count = 0
for pattern in bp_gen:
    cost = 0
    for i, p in enumerate(pattern):
        cost += w_list[a_n+i]
    if cost > X:
        continue
    b_dict[cost] += a_dict[X-cost]
    count += a_dict[X-cost]

print(f"{a_dict}")
print(f"{b_dict}")

ans = count
print(ans)
