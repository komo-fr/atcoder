#!/usr/bin/env python3

N = int(input().split()[0])
a_list = []

for _ in range(N):
    a = int(input().split()[0])
    a_list.append(a)

c = 0

for i in range(N):
    before = a_list[i - 1] if i != 0 else 0

    c += (before + a_list[i]) // 2
    a_list[i] = (before + a_list[i]) % 2 if a_list[i] != 0 else 0

ans = c
print(ans)
