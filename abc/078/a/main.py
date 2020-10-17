#!/usr/bin/env python3

X, Y = list(map(str, input().split()))
ans = "="
if X > Y:
    ans = ">"
elif X < Y:
    ans = "<"

print(ans)
