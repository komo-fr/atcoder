#!/usr/bin/env python3

A, B = list(map(int, input().split()))

ax = int(A / 0.08)
bx = int(B / 0.1)

min_x = ax
max_x = bx
x = min_x
is_ok = False
while True:
    if int(x * 0.08) == A and int(x * 0.1) == B:
        is_ok = True
        break
    if int(x * 0.08) > A or int(x * 0.1) > B:
        break
    x += 1

ans = x if is_ok else -1
print(ans)
