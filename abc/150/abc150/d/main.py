#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))
c = 0
for a in a_list:
    x = M // a
    if 2 * x - a > 0:
        c += 1
ans = c
print(ans)
