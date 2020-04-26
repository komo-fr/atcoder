#!/usr/bin/env python3

n, x = list(map(int, input().split()))
ans = min(abs(n - x), abs(x - 1))

print(ans)
