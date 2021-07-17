#!/usr/bin/env python3
import math

N = int(input().split()[0])
a_list = list(map(int, input().split()))


def calc_d(a, b):
    d = abs(a - b)
    diff = math.sqrt(1 ** 2 + d ** 2)
    return diff


S = sum(a_list)

dp = []
for i in range(N):  # x 100
    # i番目まで考えたとき
    dp.append([[None] * (S + 1) for _ in range(S + 1)])
    if i == 0:
        # 初期化
        dp[0][0][0] = 0
        continue

    for s in range(S + 1):  # 現在までの総和がsのケースについて考える  # 100
        for y in range(s + 1):  # sより大きいyは見なくてていい
            min_total_d = float("inf")
            s_pre = s - y  # 直前の総和
            for y_pre in range(s_pre + 1):  # s_preより大きいyは見なくていい
                if dp[i - 1][s_pre][y_pre] is None:
                    # NAなのでスキップ
                    continue
                new_d = calc_d(y, y_pre)  # 追加コスト
                kouho = dp[i - 1][s_pre][y_pre] + new_d
                if kouho < min_total_d:
                    # 更新
                    min_total_d = kouho

                # 確定させる
                dp[i][s][y] = min_total_d

ans = dp[-1][-1][0]
print(ans)
