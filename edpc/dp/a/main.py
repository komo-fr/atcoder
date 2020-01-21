#!/usr/bin/env python3

N = int(input().split()[0])
h_list = list(map(int, input().split()))

# 最小値を求める問題なので、infで初期化する
dp_list = [float("inf") for _ in range(N)]
dp_list[0] = 0

for i in range(1, N):
    if i - 1 >= 0:
        cost_1 = abs(h_list[i - 1] - h_list[i])
        min_cost = min(dp_list[i], dp_list[i - 1] + cost_1)

    if i - 2 >= 0:
        cost_2 = abs(h_list[i - 2] - h_list[i])
        min_cost = min(min_cost, dp_list[i - 2] + cost_2)

    dp_list[i] = min_cost

ans = dp_list[N - 1]
print(ans)
