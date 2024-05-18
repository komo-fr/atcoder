#!/usr/bin/env python3
N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))


# dp[i][j][k]
# = i日目まで考慮したとき、（今日を含め）j日間宿題をした、（今日）宿題をしたかどうかがk（0:していない、1:している）
# であるような状態の最大の楽しさとする
# (N, N, 2)サイズ
# dp = np.full((N, N+1, 2), -float("inf"))
dp = [[[-float("inf") for _ in range(2)] for _ in range(M+2)] for _ in range(N)]

# 初日に宿題をしなかった場合
dp[0][0][0] = a_list[0]  # 楽しさを得る
# 初日に宿題をした場合
dp[0][1][1] = 0

# 2日目からN日目まで考える
for i in range(1, N):  # 実際の日数はi+1日目
    # i日目について考える
    # for j in range(min(i+2, M)):  # 0〜i+1日（=最大N日）がありうる
    for j in range(min(i+2, M+2)):  # 0〜i+1日（=最大N日）がありうる
        # ここまででj日間宿題をしたケースについて考える
        # i日目に宿題をしない場合
        dp[i][j-1][0] = max([dp[i-1][j-1][0], dp[i-1][j-1][1]]) + a_list[i]

        # i日目に宿題をする場合、前日の宿題をしていないケースを持ってくる
        dp[i][j][1] = dp[i-1][j-1][0]

ans = max(dp[N-1][M])
print(int(ans))
