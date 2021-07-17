#!/usr/bin/env python3


a, b, c = list(map(int, input().split()))
d = a if a <= b * c else b * c
ans = d / b
print(ans)
