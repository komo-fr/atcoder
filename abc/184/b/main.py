#!/usr/bin/env python3
import collections

N, X = list(map(int, input().split()))
S = input()
x = X
for char in S:
    if char == "x":
        x = max(x - 1, 0)
    else:
        x += 1

ans = x
print(ans)
