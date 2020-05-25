#!/usr/bin/env python3

N = int(input().split()[0])
xlt_list = []

for _ in range(N):
    x, l = list(map(int, input().split()))
    xlt_list.append((x, l, x + l))

xlt_list = sorted(xlt_list, key=lambda x: x[2])
count = 0
before_t = -float("inf")
for i, xlt in enumerate(xlt_list):
    x, l, t = xlt
    if x - l >= before_t:
        count += 1
        before_t = t

ans = count
print(ans)
