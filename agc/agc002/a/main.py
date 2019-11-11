#!/usr/bin/env python3

a, b = list(map(int, input().split()))

if a <= 0 <= b:
    r = "Zero"
elif a > 0:
    r = "Positive"
else:
    if (b - a + 1) % 2 == 0:
        r = "Positive"
    else:
        r = "Negative"

ans = r
print(ans)
