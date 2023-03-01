#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# 値: インデックスiのマスにたどり着いた時に得られる得点の最大値
dp_list = [-float("inf")] * N
dp_list[0] = 0

for i in range(N - 1):
    # マスAに進んで100点を得る
    target_index = a_list[i] - 1
    if target_index < N:
        dp_list[target_index] = max([dp_list[i] + 100, dp_list[target_index]])

    # マスBに進んで150点を得る
    target_index = b_list[i] - 1
    if target_index < N:
        dp_list[target_index] = max([dp_list[i] + 150, dp_list[target_index]])

ans = dp_list[-1]
print(ans)
