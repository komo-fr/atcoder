#!/usr/bin/env python3
import itertools

N, M = list(map(int, input().split()))
lrs_list = []

for _ in range(N):
    l, r, s = list(map(int, input().split()))
    lrs_list.append((l, r, s))

p_gen = itertools.permutations(list(range(N)), N)
max_score = -float("inf")
for p in p_gen:
    score = 0
    m_count = 0
    m_list = []
    for n in p:
        l, r, s = lrs_list[n]
        m_list = list(set(m_list + list(range(l + 1, r + 2))))
        if len(m_list) >= M:
            break
        score += s
    max_score = max(max_score, score)

print(max_score)
