#!/usr/bin/env python3
from collections import defaultdict
import numpy as np

N, M = list(map(int, input().split()))
a_table = []
n2xy_map = defaultdict(lambda: [])
for i in range(N):
    a_list = input()
    new_a_list = []
    for a in a_list:
        if a == "S":
            new_a_list.append(0)
        elif a == "G":
            new_a_list.append(10)
        else:
            new_a_list.append(int(a))

    a_table.append(new_a_list)

    for j, a in enumerate(new_a_list):
        n2xy_map[a].append((i, j))


def calc_step(a, b) -> int:
    post_cost = abs(a[0] - b[0]) + abs(a[1] - b[1])
    pre_cost = dp[a[0]][a[1]]
    return pre_cost + post_cost


dp = np.zeros((N, M))

is_ok = True
for n in range(11):
    if not n2xy_map[n]:
        # 数字nが1個もない
        is_ok = False
        break
    if n == 0:
        # Sは飛ばす
        continue
    for n_cell in n2xy_map[n]:
        # 数字nがあるマスを巡回
        # n-1のマスからの最小距離を計算
        min_step = min([calc_step(pre_cell, n_cell) for pre_cell in n2xy_map[n - 1]])
        dp[n_cell[0]][n_cell[1]] = min_step

if is_ok:
    g = n2xy_map[10][0]  # Gは1個だけであることが保証されているので、先頭をとる
    ans = int(dp[g[0]][g[1]])
else:
    ans = -1

print(ans)
