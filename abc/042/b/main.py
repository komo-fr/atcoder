#!/usr/bin/env python3

N, L = list(map(int, input().split()))
s_list = []

for _ in range(N):
    s = input()
    s_list.append(s)
ans = "".join(sorted(s_list))

print(ans)
