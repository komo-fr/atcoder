#!/usr/bin/env python3

a, b = list(map(int, input().split()))
total = 0
x = None
for i in range(1, 999):
    left_h = total + i
    right_h = total + 2 * i + 1
    if (left_h - a) == (right_h - b):
        x = left_h - a
        break
    total += i

ans = x
print(ans)
