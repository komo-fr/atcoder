#!/usr/bin/env python3

A, B, C = list(map(int, input().split()))

ans = "NO"
for i in range(A, A * B + 1, A):
    if i % B == C:
        ans = "YES"
        break
print(ans)
