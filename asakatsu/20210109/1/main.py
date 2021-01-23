#!/usr/bin/env python3

W, a, b = list(map(int, input().split()))

if (a <= b <= a + W) or (b <= a <= b + W):
    ans = 0
else:
    ans = min([abs(b - (a + W)), abs(a - (b + W))])
print(ans)
