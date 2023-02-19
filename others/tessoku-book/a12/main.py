#!/usr/bin/env python3

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

l, r = 1, 10 ** 9

while l < r:
    t = (l + r) // 2

    # t時点における印刷枚数を計算
    total = 0
    for a in a_list:
        total += t // a

    if K <= total:
        # 左に答えがあるので、rを移動
        r = t
    else:
        # 右に答えがあるので、lを移動
        l = t + 1

ans = l
print(ans)
