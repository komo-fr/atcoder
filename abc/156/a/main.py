#!/usr/bin/env python3

N, R = list(map(int, input().split()))

if N >= 10:
    ans = R
else:
    ans = R + 100 * (10 - N)
print(ans)
