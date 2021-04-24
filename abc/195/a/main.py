#!/usr/bin/env python3

M, H = list(map(int, input().split()))

ans = "Yes" if H % M == 0 else "No"
print(ans)
