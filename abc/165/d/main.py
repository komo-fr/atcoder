#!/usr/bin/env python3
import math

A, B, N = list(map(int, input().split()))

x = min(N, B - 1)
f_1 = math.floor(A * x / B)
f_2 = A * math.floor(x / B)

score = f_1 - f_2

ans = score
print(ans)
