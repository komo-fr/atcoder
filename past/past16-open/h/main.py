#!/usr/bin/env python3
import numpy as np
N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))


# dp[i][j][k]
# = i日目まで考慮したとき、（今日を含め）j日間宿題をした、（今日）宿題をしたかどうかがk（0:していない、1:している）
# であるような状態の最大の楽しさとする
# (N, N, 2)サイズ
dp = np.full((N, N+1, 2), -float("inf"))

# 初日に宿題をしなかった場合
dp[0][0][0] = a_list[0]  # 楽しさを得る
# 初日に宿題をした場合
dp[0][1][1] = 0

# max_value = -float("inf")
# 2日目からN日目まで考える
for i in range(1, N):  # 実際の日数はi+1日目
    # i日目について考える
    for j in range(min(i+2, M+2)):  # 0〜i+1日（=最大N日）がありうる
        # ここまででj日間宿題をしたケースについて考える
        # i日目に宿題をしない場合
        dp[i][j-1][0] = max(dp[i-1][j-1][0], dp[i-1][j-1][1]) + a_list[i]

        # i日目に宿題をする場合、前日の宿題をしていないケースを持ってくる
        dp[i][j][1] = dp[i-1][j-1][0]

# デバッグ用
# for i in range(N):
#     for j in range(N + 1):
#         for k in range(2):
#             print(f"{i+1}日目に、今日を含め{j}日間宿題をしている場合に、宿題を={'した' if k else 'しなかった'}ら👉 {dp[i][j][k]}")

ans = dp[N-1][M:].max()
# ans = max_value
print(int(ans))
