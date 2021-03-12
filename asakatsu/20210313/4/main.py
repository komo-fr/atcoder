#!/usr/bin/env python3
import math

N, M = list(map(int, input().split()))
ans = (pow(10, N, M * M) // M) % M
print(ans)
