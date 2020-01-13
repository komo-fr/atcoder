#!/usr/bin/env python3

N = int(input().split()[0])
s_list = []

for _ in range(N):
    s = input()
    s = s[::-1]
    s_list.append(s)

ans = "\n".join([s[::-1] for s in sorted(s_list)])

print(ans)
