#!/usr/bin/env python3

a, b, c, d = list(map(int, input().split()))


ans = max([a * b, c * d])
print(ans)
