#!/usr/bin/env python3

import itertools

N, M, X = list(map(int, input().split()))
c_list = []
a_table = []
for _ in range(N):
    a_list = list(map(int, input().split()))
    a_table.append(a_list[1:])
    c_list.append(a_list[0])

p_list = list(itertools.product([True, False], repeat=N))
min_cost = float("inf")
for pattern in p_list:  # 4092 (10 ** 3)
    cost = 0
    rikai_list = [0] * M
    for n, is_buy in enumerate(pattern):  # N個  # 12
        # n番目の参考書
        if not is_buy:
            continue
        cost += c_list[n]
        for m, a in enumerate(a_table[n]):  # 12
            # m番目のアルゴリズム
            rikai_list[m] += a
    not_understand = [r for r in rikai_list if r < X]  # 12
    if not not_understand:
        min_cost = min(min_cost, cost)

ans = min_cost if min_cost != float("inf") else -1
print(ans)
