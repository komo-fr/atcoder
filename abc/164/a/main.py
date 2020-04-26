#!/usr/bin/env python3

s, w = list(map(int, input().split()))
ans = "unsafe" if s <= w else "safe"
print(ans)
