#!/usr/bin/env python3

A, B, C = list(map(int, input().split()))
count = 0

if A + B >= C:
    count += B + C
else:
    count += A + B
    count += B
    if C - (A + B) >= 1:
        count += 1

ans = count
print(ans)
