#!/usr/bin/env python3

X = int(input().split()[0])

ans = "No" if X == 0 or X % 100 != 0 else "Yes"
print(ans)
