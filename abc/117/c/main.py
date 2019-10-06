#!/usr/bin/env python3

N, M = list(map(int, input().split()))
x_list = list(map(int, input().split()))
x_list = sorted(x_list)
d_list = [abs(a - b) for a, b in zip(x_list[:-1], x_list[1:])]
d_list = sorted(d_list, reverse=True)

if N >= M:
    ans = 0
else:
    ans = sum(d_list[N-1:])

print(ans)
