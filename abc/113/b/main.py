#!/usr/bin/env python3

N = int(input().split()[0])
T, A = list(map(int, input().split()))
h_list = list(map(int, input().split()))
min_diff = float("inf")
target = -1

for i, h in enumerate(h_list):
    m = T - h * 0.006
    if abs(m - A) < min_diff:
        target = i + 1
        min_diff = abs(m - A)

ans = target
print(ans)
