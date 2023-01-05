#!/usr/bin/env python3

N = int(input().split()[0])
c = 0
for i in range(1, N + 1):
    c += i
    if c >= N:
        break

for x in range(1, i + 1):
    if x != c - N:
        print(x)
