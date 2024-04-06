#!/usr/bin/env python3
import bisect

N = int(input().split()[0])
a_list = list(map(int, input().split()))

# 値: その要素が末尾になる時の最長の文字列
# 更新方法: 自分より小さいAjのうち、dp[j]の最大値+1（一番長く続いているものの末尾につなげるイメージ）
dp_list = [1] * N
# 値: 長さiの部分列の末尾になり得る値の最小値
l_list = [float("inf")] * N
l_list[0] = a_list[0]

for i in range(1, N):
    x = bisect.bisect_left(l_list, a_list[i])
    dp_list[i] = x + 1
    # 長さxを満たすもののうち、最小値で更新する
    l_list[x] = a_list[i]

ans = max(dp_list)
print(ans)
