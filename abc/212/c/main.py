#!/usr/bin/env python3


N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ab_list = []
for a in a_list:
    ab_list.append((a, "a"))
for b in b_list:
    ab_list.append((b, "b"))

ab_list = sorted(ab_list)
a = None
b = None
min_y = float("inf")
for x in ab_list:
    if x[1] == "a":
        a = x[0]
    if x[1] == "b":
        b = x[0]
    if a is not None and b is not None:
        y = abs(a - b)
        min_y = min([y, min_y])

ans = min_y
print(ans)
