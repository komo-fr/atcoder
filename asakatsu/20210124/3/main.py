#!/usr/bin/env python3
from collections import Counter

N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = input()
score_dict = {"r": P, "s": R, "p": S}

# counter = Counter(T)
# ans = sum([counter[x] * score_dict[x] for x in "rsp"])
score_list = []
for i, t in enumerate(T):
    if i - K >= 0:
        if t == T[i - K] and score_list[i - K] != 0:
            score_list.append(0)
            continue
    score_list.append(score_dict[t])
ans = sum(score_list)
# print(score_list)
print(ans)
