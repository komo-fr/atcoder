#!/usr/bin/env python3
import math

N, D = list(map(int, input().split()))
xy_list = []

count = 0
for _ in range(N):
    x, y = list(map(int, input().split()))
    if math.sqrt(x ** 2 + y ** 2) <= D:
        count += 1
print(count)
