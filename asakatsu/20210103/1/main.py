#!/usr/bin/env python3

A, B = list(map(int, input().split()))


ans = A + B - 24 if A + B >= 24 else A + B
print(ans)
