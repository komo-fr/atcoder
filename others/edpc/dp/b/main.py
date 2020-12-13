#!/usr/bin/env python3
import numpy as np

N, K = list(map(int, input().split()))
h_list = list(map(int, input().split()))
h_list = np.array(h_list)
dp_list = np.zeros(N)
dp_list[0] = 0

for i in range(1, N):
    # j番目の足場からi番目の足場に飛ぶ

    min_j = max(i - K, 0)
    cost_list = dp_list[min_j:i] + np.abs(h_list[i] - h_list[min_j:i])
    # 最適コストで更新
    dp_list[i] = np.min(cost_list)

ans = int(dp_list[-1])
print(ans)
