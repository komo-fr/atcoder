#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

# シンプルな動的計画法で解く方法
# Python3、PyPy3だとTLEになる
# 値: その要素が末尾になる時の最長の文字列
# 更新方法: 自分より小さいAjのうち、dp[j]の最大値+1（一番長く続いているものの末尾につなげるイメージ）
dp_list = [1] * N

for i in range(N):
    dp_list[i] = 1
    for j in range(i):
        if a_list[j] < a_list[i]:
            dp_list[i] = max([dp_list[i], dp_list[j] + 1])

ans = max(dp_list)
print(ans)
