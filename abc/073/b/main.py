#!/usr/bin/env python3

N = int(input().split()[0])
count = 0
for _ in range(N):
    l, r = list(map(int, input().split()))
    count += r - l + 1

ans = count
print(ans)
