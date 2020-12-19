#!/usr/bin/env python3

a, b, c, d = list(map(int, input().split()))

ans = "No" if b < c or d < a else "Yes"
print(ans)
