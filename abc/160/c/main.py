#!/usr/bin/env python3

K, N = list(map(int, input().split()))
a_list = list(map(int, input().split()))

max_d = -float("inf")
total_d = 0
for i, a in enumerate(a_list):
    if i == 0:
        d = (K - a_list[-1]) + a_list[i]
    else:
        d = a_list[i] - a_list[i - 1]
    total_d += d
    max_d = max(max_d, d)
ans = total_d - max_d

print(ans)
