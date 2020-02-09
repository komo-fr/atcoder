#!/usr/bin/env python3

H, N = list(map(int, input().split()))
ab_list = []
max_a = -float("inf")
for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))
    max_a = max(max_a, a)

dp_table = [[0] + [float("inf")] * H for _ in range(N + 1)]

for i in range(1, N + 1):
    a, b = ab_list[i - 1]
    next_j = 0
    # for j in range(H + max_a):
    over_min_cost = float("inf")
    for j in range(H + 1):
        # 攻撃jをしない場合
        before_best_cost = dp_table[i - 1][j]
        dp_table[i][j] = min(dp_table[i][j], before_best_cost)
        # 攻撃jをする場合
        if j - a >= 0:
            cost = dp_table[i - 1][j - a] + b
            min_cost = min(before_best_cost, cost)

            cost = dp_table[i][j - a] + b
            min_cost = min(min_cost, cost)

            dp_table[i][j] = min(dp_table[i][j], min_cost)

        if j + a > H:
            cost = dp_table[i - 1][j] + b
            dp_table[i][H] = min(dp_table[i][H], cost)
            cost = dp_table[i][j] + b
            dp_table[i][H] = min(dp_table[i][H], cost)
            dp_table[i][H] = min(dp_table[i][H], dp_table[i - 1][H])

ans = dp_table[-1][H]
print(ans)
