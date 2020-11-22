#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
xy_list = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    xy_list.append((x, y))

p_list = list(itertools.combinations(xy_list, 3))
is_exist = False
for p in p_list:
    p1, p2, p3 = p
    t1 = (p1[0] - p2[0]) * (p3[1] - p1[1])
    t2 = (p3[0] - p1[0]) * (p1[1] - p2[1])
    if t1 == t2:
        is_exist = True
        break
ans = "Yes" if is_exist else "No"
print(ans)
