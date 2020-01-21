#!/usr/bin/env python3

N, W = list(map(int, input().split()))
item_list = []

for _ in range(N):
    w, v = list(map(int, input().split()))
    item_list.append((w, v))

max_v = (10 ** 3) * 100
dp_table = [[0] + [float("inf")] * (max_v + 1) for _ in range(N + 1)]
total_v = 0

for i in range(1, N + 1):  # 最大で10**2
    w, v = item_list[i - 1]
    # 品物iまで考慮したときの価値の最大値
    total_v += v
    for j in range(total_v + 1):  # 最大で10 ** 5
        # 品物iを入れない場合
        dp_table[i][j] = dp_table[i - 1][j]
        before_min_weight = dp_table[i - 1][j]
        # dp_table[i][j] = before_min_weight
        # 品物iを入れる場合
        if j - v < 0:
            continue
        weight = dp_table[i - 1][j - v] + w
        min_weight = min(before_min_weight, weight)
        dp_table[i][j] = min_weight
        if i == N:
            if min_weight <= W:
                max_value = j


# max_value = 0
# for i, w in enumerate(dp_table[-1]):
#     if w <= W:
#         max_value = i
ans = max_value
print(ans)
