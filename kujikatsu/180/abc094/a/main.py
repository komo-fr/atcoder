#!/usr/bin/env python3

a, b, x = list(map(int, input().split()))

ans = "YES" if a <= x <= a + b else "NO"
print(ans)
