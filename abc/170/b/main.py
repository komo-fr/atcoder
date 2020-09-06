#!/usr/bin/env python3

X, Y = list(map(int, input().split()))
is_ok = False
for i in range(0, X + 1):
    if (i * 2 + (X - i) * 4) == Y:
        is_ok = True
        break
ans = "Yes" if is_ok else "No"
print(ans)
