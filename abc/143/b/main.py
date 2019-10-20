#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
d_list = list(map(int, input().split()))
p_gen = itertools.combinations(d_list, 2)
total = 0
for p in p_gen:
    a, b = p
    total += a * b
ans = total
print(ans)
