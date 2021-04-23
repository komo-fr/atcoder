#!/usr/bin/env python3

A, B = list(map(int, input().split()))
C = A + B
if C >= 15 and B >= 8:
    ans = 1
elif C >= 10 and B >= 3:
    ans = 2
elif C >= 3:
    ans = 3
else:
    ans = 4

print(ans)
