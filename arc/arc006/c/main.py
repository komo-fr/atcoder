#!/usr/bin/env python3
import bisect

N = int(input().split()[0])
w_list = []

for _ in range(N):  # 10 ** 5
    w = int(input().split()[0])
    w_list.append(w)

tower_list = []
max_w = -float("inf")
count = 0
for w in w_list:  # 10 ** 5
    # 二分探索？
    if w > max_w:
        # 今ある荷物の上には積み重ねられない
        # 新しく山を作る
        tower_list.append(w)
        tower_list = sorted(tower_list)
        # print(tower_list)
        max_w = w
        count += 1
        continue
    # 自分より大きい中で最小の重さに載せる
    index = bisect.bisect_left(tower_list, w)
    # print(index)
    tower_list[index] = w
    # print(tower_list)
    tower_list = sorted(tower_list)
    max_w = tower_list[-1]
ans = count
print(ans)
