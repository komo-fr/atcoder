#!/usr/bin/env python3
import math

a, b = list(map(int, input().split()))
ans = None
if a > 0 and b > 0:
    ans = "Positive"
elif a == 0 or b == 0 or (a <= 0 <= b):
    ans = "Zero"
else:
    if (b - a + 1) % 2 == 0:
        ans = "Positive"
    else:
        ans = "Negative"

print(ans)
