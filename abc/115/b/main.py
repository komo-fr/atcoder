#!/usr/bin/env python3

N = int(input().split()[0])
p_list = []

for _ in range(N):
    p = int(input().split()[0])
    p_list.append(p)

p_list = sorted(p_list, reverse=True)
ans = p_list[0] // 2 + sum(p_list[1:])

print(ans)
