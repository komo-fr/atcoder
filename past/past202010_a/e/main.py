#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
S = input()
p_list = list(itertools.permutations(S, N))
r_s = S[::-1]
T = "None"
for pattern in p_list:
    t = "".join(pattern)
    if t not in [S, r_s]:
        T = t
        break
ans = T
print(ans)
