#!/usr/bin/env python3
import bisect
import numpy as np

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))
bc_list = []

for i in range(M):
    b, c = list(map(int, input().split()))
    bc_list.append((b, c))

bc_list = sorted(bc_list, key=lambda x: x[1], reverse=True)
a_list = sorted(a_list)

fix_list = []
s = 0
b, c = bc_list[0]
bc_index = 0
count_b = 0

for a in a_list:
    if count_b >= b:
        bc_index += 1
        if bc_index >= len(bc_list):
            s += a
            continue
        count_b = 0
        b, c = bc_list[bc_index]

    if a < c:
        s += c
    else:
        s += a
    count_b += 1

ans = s
print(ans)
