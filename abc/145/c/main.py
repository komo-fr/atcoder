#!/usr/bin/env python3
import itertools
import math

N = int(input().split()[0])
xy_list = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    xy_list.append((x, y))

l = list(range(N))
p_list = list(itertools.permutations(l))
m_list = []
total = 0
count = 0
for p in p_list:
    count += 1
    t = 0
    for i, a in enumerate(p[:-1]):
        ax, ay = xy_list[a]
        bx, by = xy_list[p[i + 1]]
        t += ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
    total += t

ans = total / count

print(ans)
