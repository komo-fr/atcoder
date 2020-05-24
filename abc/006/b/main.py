#!/usr/bin/env python3

N = int(input().split()[0])
mod = 10007
a_list = []
for i in range(N):
    if i == 0:
        a_list.append(0)
    elif i == 1:
        a_list.append(0)
    elif i == 2:
        a_list.append(1)
    else:
        a = a_list[i - 1] % mod + a_list[i - 2] % mod + a_list[i - 3] % mod
        a_list.append(a)

ans = a_list[-1] % mod

print(ans)
