#!/usr/bin/env python3
# https://atcoder.jp/contests/abc031/tasks/abc031_c
# C - 数列ゲーム
import itertools
N = int(input().split()[0])
a_list = list(map(int, input().split()))

a_best_scores_list = []

for t_i in range(N):
    aoki_best = - float('inf')
    scores = (- float('inf'), - float('inf'))
    for a_i in range(N):
        if a_i == t_i:
            continue
        t, a = 0, 0
        s = min(t_i, a_i)
        e = max(t_i, a_i)
        w_list = a_list[s: e+1]

        for i, w in enumerate(w_list):
            if i % 2 == 0:
                t += w
            else:
                a += w

        # 「ベストスコアが複数の場合は一番左側を選ぶ」ので
        # =は含めない
        if a > aoki_best:
            aoki_best = a
            scores = (t, a)

    a_best_scores_list.append(scores)

t_best = max([scores[0] for scores in a_best_scores_list])
ans = t_best
print(ans)
