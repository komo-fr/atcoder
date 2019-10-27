#!/usr/bin/env python3
import numpy as np

a, b, x = list(map(int, input().split()))
a *= 1000
b *= 1000
x *= 1000000000

Y = a * a * b - x
h = (2 * Y) / (a * a)

# ans = np.arctan2(h, a) * 180 / np.pi
ans = np.arctan2(h, a)
ans = np.rad2deg(ans)

if h > b:
    h = (2 * x) / (a * b)
    # ans = np.arctan2(b, h) * 180 / np.pi
    ans = np.arctan2(b, h)
    ans = np.rad2deg(ans)

print(ans)
