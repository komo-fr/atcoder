#!/usr/bin/env python3
N, T = list(map(int, input().split()))
ab_list = []
weight = []
value = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    weight.append(a)
    value.append(b)

#  DPテーブル
dp = [[0] * (T - 1) for _ in range(N + 1)]
dp_3 = []
max_v = -float("inf")

for j in range(N):
    w_last = weight[j]
    v_last = value[j]
    for i in range(N):
        if i == j:
            continue
        for w in range((T - 1)):
            if w >= weight[i]:
                dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
            else:
                dp[i + 1][w] = dp[i][w]
    max_v = max(max_v, dp[N - 1][T - 2] + v_last)
ans = max_v
print(ans)
