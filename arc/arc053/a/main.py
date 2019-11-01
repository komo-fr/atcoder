#!/usr/bin/env python3

H, W = list(map(int, input().split()))

if H == 1 and W == 1:
    ans = 0
elif H == 1 or W == 1:
    ans = max(H, W) - 1
else:
    ans = (W - 1) * H + (H - 1) * W

print(ans)
