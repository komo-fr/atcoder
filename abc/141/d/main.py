#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))

for _ in range(M):
    a_list = sorted(a_list, reverse=True)
    a_list[0] = a_list[0] // 2

ans = sum(a_list)
print(ans)
