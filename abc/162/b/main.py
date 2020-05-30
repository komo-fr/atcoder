#!/usr/bin/env python3

N = int(input().split()[0])
total = 0

for i in range(1, N + 1):
    if i % 5 != 0 and i % 3 != 0:
        total += i

ans = total
print(ans)
