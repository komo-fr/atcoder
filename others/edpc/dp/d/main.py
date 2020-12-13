#!/usr/bin/env python3

N, W = list(map(int, input().split()))
item_list = []

for _ in range(N):
    w, v = list(map(int, input().split()))
    item_list.append((w, v))

dp_table = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = item_list[i - 1]
    for j in range(W + 1):
        # 品物iを入れない場合
        before_best_value = dp_table[i - 1][j]
        dp_table[i][j] = before_best_value
        # 品物iを入れる場合
        if j - w < 0:
            continue
        value = dp_table[i - 1][j - w] + v
        best_value = max(before_best_value, value)
        dp_table[i][j] = best_value

ans = max(dp_table[-1])
print(ans)
