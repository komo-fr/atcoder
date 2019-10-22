#!/usr/bin/env python3

N, T = list(map(int, input().split()))
ct_list = []

for _ in range(N):
    c, t = list(map(int, input().split()))
    ct_list.append((c, t))

min_c = float("inf")

for ct in ct_list:
    c, t = ct
    if t <= T:
        min_c = min(c, min_c)

ans = min_c if min_c != float("inf") else "TLE"
print(ans)
