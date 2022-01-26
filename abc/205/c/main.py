#!/usr/bin/env python3

a, b, c = list(map(int, input().split()))
if a == b:
    ans = "="
elif a < b:
    ans = "<"
    if a < 0 and b >= 0 and c % 2 == 0 and c != 0:
        ans = "<" if abs(a) < abs(b) else ">"
        ans = "=" if abs(a) == abs(b) else ans
    if a < 0 and b < 0 and c % 2 == 0 and c != 0:
        ans = ">"
        ans = "=" if abs(a) == abs(b) else ans
else:
    ans = ">"
    if a >= 0 and b < 0 and c % 2 == 0 and c != 0:
        ans = ">" if abs(b) < abs(a) else "<"
        ans = "=" if abs(a) == abs(b) else ans
    if a < 0 and b < 0 and c % 2 == 0 and c != 0:
        ans = "<"
        ans = "=" if abs(a) == abs(b) else ans

print(ans)
