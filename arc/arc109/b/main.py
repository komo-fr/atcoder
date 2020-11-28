#!/usr/bin/env python3
import math

N = int(input().split()[0])

x = int(math.sqrt(2 * (N + 1)))

if x * (1 + x) > 2 * (N + 1):
    x = x - 1

ans = N - x + 1
print(ans)
