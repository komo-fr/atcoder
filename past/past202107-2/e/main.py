#!/usr/bin/env python3

N = int(input().split()[0])
K = -1
for k in range(1, 31):
    x = 1
    for i in range(1, 31):
        x = x * 3
        if i == k:
            x += 1
    if x == N:
        K = k
        break
ans = K
print(ans)
