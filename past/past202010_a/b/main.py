#!/usr/bin/env python3
import math

x, y = list(map(int, input().split()))

if y == 0:
    ans = "ERROR"
else:
    w = math.floor(x / y * 100) / 100
    w_s = str(w).split(".")
    if len(w_s[1]) < 2:
        ans = str(w) + "0" * (2 - len(w_s[1]))
    else:
        ans = w

print(ans)
