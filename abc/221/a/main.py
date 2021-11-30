#!/usr/bin/env python3

A, B = list(map(int, input().split()))


ans = 32 ** (A - B)
print(ans)
