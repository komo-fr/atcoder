#!/usr/bin/env python3

A, K = list(map(int, input().split()))

t = A
d = 0

while t < 2 * 10 ** 12:
    t += 1 + K * t
    d += 1

print(d)
