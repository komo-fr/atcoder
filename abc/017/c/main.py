#!/usr/bin/env python3
import itertools

N, M = list(map(int, input().split()))
lrs_list = []

for _ in range(N):
    l, r, s = list(map(int, input().split()))
    lrs_list.append((l, r, s))

# 最後に得る宝石は何か、で考える
max_score = -float("inf")
imos_list = [0] * (M + 1)
total = 0
for n in range(N):
    l, r, s = lrs_list[n]
    imos_list[l - 1] += s
    imos_list[r] -= s
    total += s

cumsum_list = [0] * M
before = 0
for m in range(M):
    cumsum_list[m] = before + imos_list[m]
    before = cumsum_list[m]

ans = total - min(cumsum_list)
print(ans)
