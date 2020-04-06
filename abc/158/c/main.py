#!/usr/bin/env python3

A, B = list(map(int, input().split()))
x = -1
for i in range(1, 10000):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        x = i
        break

ans = x
print(ans)
