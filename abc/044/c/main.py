#!/usr/bin/env python3

import itertools

N, A = list(map(int, input().split()))
x_list = list(map(int, input().split()))

max_x = max(max(x_list), A)
dp = [[[0 for s in range(N * max_x + 1)] for k in range(N + 1)] for j in range(N + 1)]
dp[0][0][0] = 1
ka_list = []

for j in range(N + 1):  # 何番目の数か
    x = x_list[j - 1]
    for k in range(N + 1):  # k枚選ぶとき
        for s in range(N * max_x + 1):
            if j == 0 and k == 0 and s == 0:
                dp[0][0][0] = 1
            elif j >= 1 and s < x:
                # オーバーするので選べない
                # ひとつ前と同じになる
                dp[j][k][s] = dp[j - 1][k][s]
            elif j >= 1 and k >= 1 and s >= x:
                dp[j][k][s] = dp[j - 1][k][s] + dp[j - 1][k - 1][s - x]
            else:
                dp[j][k][s] = 0

ans = sum([dp[N][k][k * A] for k in range(1, N + 1)])
print(ans)
