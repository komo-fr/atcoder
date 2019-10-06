#!/usr/bin/env python3

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

c = 0
# i - j番目までの部分列の総和がK以上のとき
# i - (j + 1)番までの部分列の総和もK以上になる
# 左端iを固定して右端を伸ばして計算する
w = 0
r = 0
next_start_r = 0
for l in range(N):
    while w < K:
        if r == N:
            break
        w += a_list[r]
        r += 1
    if w >= K:
        # 残りの右側の数
        c += N - r + 1
    # 最初の左端を引く
    w -= a_list[l]

ans = c
print(ans)
