#!/usr/bin/env python3
import math

H = int(input().split()[0])
c = 0
now_h = H
i = 0
while now_h >= 1:
    now_h = now_h // 2
    if i == 0:
        c += 1
    else:
        c += 2 ** i
    i += 1

ans = c
print(ans)
