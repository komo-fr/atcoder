#!/usr/bin/env python3
from collections import defaultdict

N = int(input().split()[0])
c = input()
counter = defaultdict(int)

for i in range(N - 1):
    command = c[i] + c[i + 1]
    counter[command] += 1

min_count = float("inf")

for k, v in sorted(counter.items()):
    for kk, vv in sorted(counter.items()):
        s = c.replace(k, "L").replace(kk, "R")
        min_count = min(min_count, len(s))

ans = min(min_count, len(c))
print(ans)
