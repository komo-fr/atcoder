#!/usr/bin/env python3

a, b, c = list(map(int, input().split()))

if a == b:
    ans = "Takahashi" if c != 0 else "Aoki"
else:
    ans = "Takahashi" if a > b else "Aoki"

print(ans)
