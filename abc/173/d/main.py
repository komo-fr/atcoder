#!/usr/bin/env python3
from collections import deque

N = int(input().split()[0])
a_list = list(map(int, input().split()))
a_list = sorted(a_list, reverse=True)

c_list = a_list[: (N + 1) // 2]

if len(c_list) == 1:
    ans = c_list[0]
elif N % 2 == 0:
    ans = c_list[0] + sum(c_list[1:]) * 2
else:
    ans = c_list[0] + sum(c_list[1:-1]) * 2 + c_list[-1]

print(ans)
