#!/usr/bin/env python3
n = int(input().split()[0])
s, t = list(input().split())

ans = ""
for c1, c2 in zip(s, t):
    ans = ans + c1 + c2

print(ans)
