#!/usr/bin/env python3
import math

A, R, N = list(map(int, input().split()))
# a = A * (R ** (N - 1))
# ans = a if a <= 10 ** 9 else "large"
ans = A * (R ** (N - 1)) if N <= math.log((10 ** 9 / A), R) + 1 else "large"

print(ans)
