#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))

for _ in range(M):
    max_diff = -float("inf")
    max_index = 0
    for i, a in enumerate(a_list):
        if a - (a // 2) > max_diff:
            max_diff = a - (a // 2)
            max_a = a // 2
            max_index = i
    a_list[max_index] = max_a

ans = sum(a_list)
print(ans)
