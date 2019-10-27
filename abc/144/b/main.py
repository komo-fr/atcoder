#!/usr/bin/env python3

N = int(input().split()[0])
is_ok = False
for x in range(1, 10):
    if N % x == 0:
        if 1 <= N // x <= 9:
            is_ok = True
            break

ans = "Yes" if is_ok else "No"
print(ans)
