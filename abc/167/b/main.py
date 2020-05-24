#!/usr/bin/env python3

A, B, C, K = list(map(int, input().split()))
k = K
t = 0

t += min(k, A)
k -= min(k, A)


if k > 0 and B > 0:
    k -= min(k, B)

if k > 0 and C > 0:
    t -= min(k, C)
    k -= min(k, C)

ans = t
print(ans)
