#!/usr/bin/env python3
import itertools
N, K = list(map(int, input().split()))
d_table = []

for i in range(N):
    d_list = list(map(int, input().split()))
    d_table.append(d_list)
# print(d_table)
p_gen = itertools.permutations(range(1, N), N-1)
count = 0
for pattern in p_gen:
    cost = 0
    for k in range(N-2):
        i = pattern[k]
        j = pattern[k + 1]
        cost += d_table[i][j]
    else:
        cost += d_table[pattern[-1]][0]
        cost += d_table[0][pattern[0]]

    if cost == K:
        count += 1
ans = count
print(ans)
