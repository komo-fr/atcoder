#!/usr/bin/env python3
import bisect


N = int(input().split()[0])
l_list = list(map(int, input().split()))
l_list = sorted(l_list)
p_list = []

for a_i, a in enumerate(l_list):
    for b_i, b in enumerate(l_list):
        if a_i == b_i:
            continue
        for c_i, c in enumerate(l_list):
            if c_i == b_i or c_i == a_i:
                continue
            # if a < b + c and b < c + a and c < a + b:
            #     p_list += [sorted([a, b, c])]
            if a - c < b < a + b:
                p_list += [sorted([a, b, c])]

p_list = ["{}_{}_{}".format(p[0], [1], [2]) for p in p_list]
ans = len(set(p_list))

print(ans)
