#!/usr/bin/env python3

A, B = list(map(int, input().split()))
ans = max([A + B, A - B, A * B])
print(ans)
