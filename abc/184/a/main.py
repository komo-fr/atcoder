#!/usr/bin/env python3

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

ans = a * d - b * c
print(ans)
