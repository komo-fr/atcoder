#!/usr/bin/env python3

N, Q = list(map(int, input().split()))

tk_list = []
for _ in range(Q):
    t, k = list(map(int, input().split()))
    tk_list.append((t, k))

cond_list = []

# 出力クエリのたびに反転回数を数える方法（TLE）
for t, k in tk_list:
    if t == 2:
        cond_list.append(((N - k + 1), (N + k)))

cond_list = sorted(cond_list)
cond_index = 0
next_cond = cond_list[cond_index]
r_count = 0
for i in range(2*N):
    if i+1 < next_cond[0]