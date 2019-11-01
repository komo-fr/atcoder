#!/usr/bin/env python3
import math

A, K = list(map(int, input().split()))

goal = 2 * 10 ** 12

if K == 0:
    d = goal - A
else:
    d = 0
    t = A
    while t < goal:
        t += 1 + t * K
        d += 1

print(d)
