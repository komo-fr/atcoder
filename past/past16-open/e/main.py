#!/usr/bin/env python3

N = input().strip()
keta = len(N)

if N == "1" + "0" * (keta-1):
    ans = keta - 1
else:
    ans = keta
print(ans)