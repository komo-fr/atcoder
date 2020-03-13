#!/usr/bin/env python3

N = int(input().split()[0])
total = 0
for i in range(1, N + 1):  # max = 200
    a = i
    if a % 2 == 0:
        continue
    c = 0
    for j in range(1, N + 1):  # max = 200
        if a % j == 0:
            c += 1
    if c == 8:
        total += 1
ans = total
print(ans)
