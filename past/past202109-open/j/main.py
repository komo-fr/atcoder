#!/usr/bin/env python3

N, Q = list(map(int, input().split()))

tk_list = []
for _ in range(Q):
    t, k = list(map(int, input().split()))
    tk_list.append((t, k))

cond_list = []

# 出力クエリのたびに反転回数を数える方法（TLE）
for t, k in tk_list:
    if t == 1:
        # 出力
        r_count = 0
        for cond in cond_list:
            if cond[0] <= k <= cond[1]:
                r_count += 1
        # print(f"反転回数: {r_count=}")
        if r_count % 2 == 0:
            print(k)
        else:
            print(2 * N - k + 1)
    else:
        cond_list.append(((N - k + 1), (N + k)))
