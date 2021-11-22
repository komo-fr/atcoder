#!/usr/bin/env python3

s, t, x = list(map(int, input().split()))

ans = "No"
if s < t and s <= x < t:
    ans = "Yes"
if s > t and (x >= s or x < t):
    ans = "Yes"

print(ans)
