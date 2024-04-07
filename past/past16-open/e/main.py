#!/usr/bin/env python3

N = int(input().split()[0])
keta = len(str(N))

if N == 10 ** (keta-1):
    ans = keta -1
else:
    ans = keta

print(ans)