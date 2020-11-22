#!/usr/bin/env python3

N = int(input().split()[0])
ab_list = []
t = 0
for _ in range(N):
    a, b = list(map(int, input().split()))
    t += (1 / 2) * ((b - a + 1) * (a + b))

ans = int(t)
print(ans)
