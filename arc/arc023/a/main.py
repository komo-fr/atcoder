#!/usr/bin/env python3
import math

y = int(input().split()[0])
m = int(input().split()[0])
d = int(input().split()[0])


def calc(y, m, d):
    y = y - 1 if m in [1, 2] else y
    m = 12 + m if m in [1, 2] else m
    return 365 * y + y // 4 - y // 100 + y // 400 + (306 * (m + 1)) // 10 + d - 429


start = calc(y, m, d)
end = calc(2014, 5, 17)
ans = end - start
print(ans)
