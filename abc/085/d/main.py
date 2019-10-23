#!/usr/bin/env python3
import math

N, H = list(map(int, input().split()))
ab_list = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

k_list = sorted(ab_list, key=lambda x: (x[1], -x[0]), reverse=True)
count = 0

# bが最大の刀のa
max_b_a, max_b = k_list[0][0], k_list[0][1]
# 最大のa
max_a, max_a_b = sorted(k_list, key=lambda x: (x[0], -x[1]), reverse=True)[0]

while H > 0:
    if max_a >= max_b:
        # (B)(D)パターン
        # 4, 5
        # 10, 6
        # や
        # 10, 5
        # 3, 6
        # 投げるより普通に殴った方が良いので迷わず殴る
        count += H // max_a
        count = count + 1 if H % max_a != 0 else count
        break

    # 以下、a < bが担保されている
    # あと1発で倒せる場合は迷わず投げる
    if H - max_b <= 0:
        H -= max_b
        count += 1
        break

    # Select Katana
    if len(k_list) == 1:
        # あと1本しかない場合は、投げるのは温存して殴るしかない
        # 3, 5
        count += 1  # 投げるターンの1回
        count += (H - k_list[0][1]) // k_list[0][0]
        count = count + 1 if (H - k_list[0][1]) % k_list[0][0] != 0 else count
        break

    if max_a == max_b_a and k_list[0][0] > k_list[1][1]:
        # (E)パターン
        count += 1  # 投げるターンの1回
        count += (H - k_list[0][1]) // k_list[0][0]
        count = count + 1 if (H - k_list[0][1]) % k_list[0][0] != 0 else count
        break

    if max_a >= max_b_a and max_a_b != max_b:
        # (A)パターン
        # max_aより大きいbがあれば積極的に投げ続ける
        # (E)パターンに移行するか、Hが0になるまでやる
        # 他に殴り力が高い刀があるので、投げ力が高い刀でも迷いなく投げていい
        # a < b は担保されている
        # 4, 5
        # 3, 6
        H -= max_b
        k_list.pop(0)
        count += 1
        # 更新
        max_b_a, max_b = k_list[0][0], k_list[0][1]
        # max_a, _ = sorted(k_list, key=lambda x: (x[0], -x[1]), reverse=True)[0]
        continue

    # 殴り力でも投げ力でも1位
    # ただし殴り力1位が投げ力2位より高いとは限らない
    if max_b_a >= k_list[1][0]:
        # (E)パターン
        # 殴り力1位が投げ力2位より高い場合、最後に投げるまで殴り続けた方が良い
        # 2, 4
        # 5, 6
        count += 1
        count += (H - k_list[0][1]) // k_list[0][0]
        count = count + 1 if (H - k_list[0][1]) % k_list[0][0] != 0 else count
        break
    else:
        # (C)パターン
        # 殴り力1位が投げ力2位より低い場合、積極的に投げる
        # 2, 5
        # 4, 6
        H -= k_list[1][1]
        k_list.pop(1)
        count += 1
        # 更新
        max_b_a, max_b = k_list[0][0], k_list[0][1]
        # max_a, _ = sorted(k_list, key=lambda x: (x[0], -x[1]), reverse=True)[0]

ans = count
print(ans)
