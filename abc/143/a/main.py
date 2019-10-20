#!/usr/bin/env python3

a, b = list(map(int, input().split()))
ans = max(a - b * 2, 0)
print(ans)
