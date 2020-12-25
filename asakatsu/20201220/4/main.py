#!/usr/bin/env python3
from collections import Counter

N = int(input().split()[0])
S = input()
mod = 10 ** 9 + 7
counter = Counter(S)
c = 1
for k, v in counter.items():
    c *= v + 1
    c = c % mod

ans = (c - 1) % mod
print(ans)
