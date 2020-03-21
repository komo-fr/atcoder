#!/usr/bin/env python3
import itertools

N, M = list(map(int, input().split()))
a_table = []
c = 0
for _ in range(N):
    a_list = list(map(int, input().split()))
    a_table.append(a_list)

p_gen = itertools.combinations(range(M), 2)
max_score = -float("inf")
for p in p_gen:
    a, b = p
    temp_score = 0
    for a_list in a_table:
        temp_score += max(a_list[a], a_list[b])
    max_score = max(temp_score, max_score)
print(max_score)
