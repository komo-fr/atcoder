#!/usr/bin/env python3
import math

A, K = list(map(int, input().split()))

goal_t = 2 * 10 ** 12
t = A
if K == 0:
    x = goal_t - A
else:
    x = 0
    while t < goal_t:
        x += 1
        t = t + (1 + K * t)

ans = x
print(ans)
