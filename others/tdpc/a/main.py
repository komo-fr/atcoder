#!/usr/bin/env python3
import numpy as np

N = int(input().split()[0])
p_list = list(map(int, input().split()))

# 0 = 存在しない、1 = 存在する
dp = np.zeros((N + 1, sum(p_list) + 2))
dp[0][0] = 1
for i, p in enumerate(p_list):
    # i番目の問題まで考える
    for j, flag in enumerate(dp[i + 1]):
        if dp[i][j] == 1:
            dp[i + 1][j] = 1
            continue
        if j - p >= 0 and dp[i][j - p] == 1:
            dp[i + 1][j] = 1

ans = int(dp[-1].sum())
print(ans)
