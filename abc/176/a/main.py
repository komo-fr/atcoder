#!/usr/bin/env python3
import math

N, X, T = list(map(int, input().split()))

ans = math.ceil(N / X) * T

print(ans)
