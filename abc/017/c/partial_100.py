#!/usr/bin/env python3
import itertools

N, M = list(map(int, input().split()))
lrs_list = []

for _ in range(N):
    l, r, s = list(map(int, input().split()))
    lrs_list.append((l, r, s))

# 最後に得る宝石は何か、で考える
max_score = -float("inf")
for m in range(1, M + 1):
    score = 0
    # 宝石mが含まれる遺跡は選ばない
    for n in range(N):
        l, r, s = lrs_list[n]
        if l <= m <= r:
            continue
        score += s
    max_score = max(max_score, score)

ans = max_score
print(ans)
