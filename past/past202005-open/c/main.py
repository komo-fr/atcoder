#!/usr/bin/env python3
import math

A, R, N = list(map(int, input().split()))
if R == 1:
    ans = A if A <= 10 ** 9 else "large"
else:
    ans = A * (R ** (N - 1)) if N <= math.log((10 ** 9 / A), R) + 1 else "large"

print(ans)
