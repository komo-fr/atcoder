#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
l_list = list(map(int, input().split()))

p_gen = itertools.combinations(range(len(l_list)), 3)
tri_list = []
for pattern in p_gen:
    i, j, k = sorted(list(pattern))
    w_list = sorted([l_list[i], l_list[j], l_list[k]])
    if len(set(w_list)) == 3:
        if w_list[2] < w_list[0] + w_list[1]:
            tri_list.append((i, j, k))
ans = len(tri_list)
print(ans)
