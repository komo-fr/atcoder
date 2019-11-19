#!/usr/bin/env python3
import collections

N = int(input().split()[0])
r = input()
c = collections.Counter(r)
s = 0

for i, char in enumerate("FDCBA"):
    s += c[char] * i

ans = s / len(r)
print(ans)
