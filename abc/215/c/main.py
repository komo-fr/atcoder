#!/usr/bin/env python3
import itertools

S, K = list(input().split())

p_gen = itertools.permutations(S, len(S))
s_list = []
for p in p_gen:
    s_list.append("".join(p))
s_list = list(set(s_list))
ans = sorted(s_list)[int(K) - 1]
print(ans)
